import sys
import os
from dotenv import load_dotenv

load_dotenv(".env")

PROJECT_DIRECTORY = os.getenv("PROJECT_DIRECTORY")
sys.path.insert(1, PROJECT_DIRECTORY)

from langchain_core.messages import HumanMessage
from state import State
from choose_philosophy import choose_philosophy
from eastern_guru import eastern_guru
from stoic_tutor import stoic_tutor
from existentialist import existentialist
from diagnostician import diagnostician
from prescriber import prescriber
from happiness import happy_agent

prompt = HumanMessage(content="My foot hurts.", name="human")
philosopher = "eastern_guru"

state = {
    "messages": [prompt],
    "philosopher": philosopher,
}

state = choose_philosophy(state)
print("### philosophy response: ", state)
state = happy_agent(state)
print("\n### happy score: ", state)
state = diagnostician(state)
print("\n### diagnosis: ", state)
state = prescriber(state)
print("\n### prescription: ", state)

