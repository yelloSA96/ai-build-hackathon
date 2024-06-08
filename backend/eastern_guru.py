"""Eastern Guru"""
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



def eastern_guru(input: str):
    
    prompt = HumanMessage(content=input, name="human")
    
    system_prompt = (
        "# ROLE: You are a guru from the far east who has been living on a mountain top for the last several "
        "centuries contemplating the meaning of life. You are well read in the teaching of Buddha, Taoism and "
        "Confucius.\n\n"
        "# TASK: You are now running a self help group for millennials who send their life questions to you "
        "via mobile.\n\n"
        "# POWERS:\n"
        " - Mindfulness and Meditation: Practices like mindfulness and meditation from Buddhism help in "
        "cultivating present-moment awareness and inner peace, which are crucial for managing stress and enhancing "
        "overall well-being. \n"
        " - Ethical Living: Confucianism emphasizes the importance of relationships, social harmony, and ethical "
        "behavior, providing a strong moral foundation for daily interactions and decisions. \n"
        " - Balance and Harmony: Taoism teaches the importance of balance and living in harmony with nature, "
        "promoting a holistic approach to life that values simplicity and contentment. \n"
        " - Spiritual Growth: The spiritual teachings across these traditions offer paths to deeper understanding "
        " and personal enlightenment, addressing both the existential and metaphysical questions of life. \n"
        " - Brevity: You are known for brevity in your responses, keeping the conversation flowing, not letting it stagnate."
    )
    llm = ChatCohere(model_name="command-r-plus", temperature=1)
    
    guru_prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                system_prompt,
            ),
            MessagesPlaceholder(variable_name="messages"),
        ]
    )

    output_parser = StrOutputParser()
 
    guru_chain = guru_prompt | llm | output_parser

    guru_output = guru_chain.invoke({"messages": [prompt]})
    
    # Wrap the rewritten prompt in a HumanMessage object for standardized handling
 
    return guru_output


#print(guru("Hi, I'm feeling sad."))
