"""
Agent that determines when the Human has had enough!
"""
import sys
import os
from dotenv import load_dotenv

load_dotenv()

PROJECT_DIRECTORY = os.getenv("PROJECT_DIRECTORY")
sys.path.insert(1, PROJECT_DIRECTORY)  # Include project directory in the system path for module imports

from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from langchain_cohere import ChatCohere

class KeepGoing(BaseModel):
    """Data model for checking if the human wants to keep talking to the philosopher."""
    # response: str = Field(description="The human's response to the re-engineered prompt.")
    Continue: str = Field(description="Whether the human wants to continue")

def end_agent(state):

    messages = state["messages"]
    end_agent_preamble = (
        "You are an expert at interpreting human sentiment and when they want to stop talking to their pocket philosopher."
        "'End' - If they say anything that is likely to be interpreted as them wanting to stop the conversation. \n"
        "'Continue' - For any other response."
    )

    # Initialize the language model with zero randomness for consistent outputs
    llm = ChatCohere(model="command-r-plus", temperature=0)
    structured_llm = llm.with_structured_output(KeepGoing, preamble=end_agent_preamble)

    end_agent_prompt = ChatPromptTemplate.from_messages(
        [("human", "Response that needs to be analysed: {messages}")]
    )

    end_agent_chain = end_agent_prompt | structured_llm  # Chain the prompt template with the structured language model

    #not sure if human response needs []
    end_agent_response = end_agent_chain.invoke({"messages": messages})
    
    end_agent_decision = end_agent_response.Continue

    return end_agent_decision
