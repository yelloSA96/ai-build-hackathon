"""
Module for analysing hapiness
"""
import sys
import os
from dotenv import load_dotenv

load_dotenv(".env")

PROJECT_DIRECTORY = os.getenv("PROJECT_DIRECTORY")
sys.path.insert(1, PROJECT_DIRECTORY)

from langchain_core.output_parsers import StrOutputParser
from langchain_cohere import ChatCohere
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage



def happy_agent(state):
    
    messages = state["messages"]
    
    system_prompt = (
        "# ROLE: You are an expert at analysing the happiness of a person. \n\n"
        "# TASK: You will be presented with a conversation between a human and their philosopher. "
        " Your job is to analyse the conversation and rate the humans happiness.\n\n"
        "# NOTES:\n"
        " - Always return a numerical value with maximum of 100."
        " - Whole numbers only."
        " - Negative values are sad."
        " - Positive values are happy."
    )
    llm = ChatCohere(model_name="command-r-plus", temperature=1)
    
    happy_prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                system_prompt,
            ),
            MessagesPlaceholder(variable_name="messages"),
        ]
    )

    output_parser = StrOutputParser()
 
    happy_chain = happy_prompt | llm | output_parser

    happy_output = happy_chain.invoke({"messages": messages})
    
    state["happiness_score"] = happy_output
 
    return state


#print(happy_agent("Hi, I'm feeling sad."))
