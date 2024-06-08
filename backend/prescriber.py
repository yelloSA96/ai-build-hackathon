"prescriber"

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



def prescriber(input: str):
    
    prompt = HumanMessage(content=input, name="human")
    
    system_prompt = (
        "# ROLE: You are an expert at prescribing treatments. \n\n"
        "# TASK: Your task is to prescribe a treatment for the human based on their diagnosis. \n"
        "# NOTES:\n"
        " - You always return a treatment and only a treatment."
        " - You are known for being thorough and accurate."
        " - You are known for being honest and transparent."
        " - You are known for being empathetic and understanding."
        " - You are known for being patient and understanding."
        " - You are known for being helpful and supportive."
    )
    llm = ChatCohere(model_name="command-r-plus", temperature=1)
    
    prescriber_prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                system_prompt,
            ),
            MessagesPlaceholder(variable_name="messages"),
        ]
    )

    output_parser = StrOutputParser()
 
    prescriber_chain = prescriber_prompt | llm | output_parser

    prescriber_output = prescriber_chain.invoke({"messages": [prompt]})
    
    # Wrap the rewritten prompt in a HumanMessage object for standardized handling
 
    return prescriber_output

#print(prescriber("You have a broken foot."))
