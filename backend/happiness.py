"""
Module for analysing hapiness
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

# LangChain's BaseModel and Field are derived from pydantic's BaseModel class and Field attribute and can be used to
# enforce structure in an LLM's responses. Here we are using them to ensure that the LLM only responds in one of two
# ways. This can be extremely useful in flow engineering as it allows us to route the flow to the correct node
# without having to worry about variances in the LLM's responses.
class AnalyserResponse(BaseModel):
    """Data model for analysing the human's response."""
    # response: str = Field(description="The human's response to the re-engineered prompt.")
    next_action: str = Field(description="The next action to be taken: 'Proceed' or 'Try Again'")

def analyser(state):

    analyser_preamble = (
        "You are an analyst that assesses the user's response to the re-engineered prompt and assigns it to one of the following values: \n"
        "'Proceed' - for responses that are affirmitive and are agreeable to the re-engineered prompt. \n"
        "'Try Again' - for all other responses, including responses requesting any change, clarification or modification to the prompt. \n"
    )

    # Initialize the language model with zero randomness for consistent outputs
    llm = ChatCohere(model="command-r", temperature=0)
    structured_llm = llm.with_structured_output(AnalyserResponse, preamble=analyser_preamble)

    analyser_prompt = ChatPromptTemplate.from_messages(
        [("human", "Response that needs to be analysed: {messages}")]
    )

    analyser_chain = analyser_prompt | structured_llm  # Chain the prompt template with the structured language model

    return analyser_chain