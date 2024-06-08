"""Function for choosing a philosophy for the human to interact with."""
import sys
import os
from dotenv import load_dotenv

load_dotenv(".env")

PROJECT_DIRECTORY = os.getenv("PROJECT_DIRECTORY")
sys.path.insert(1, PROJECT_DIRECTORY)

from eastern_guru import eastern_guru
from stoic_tutor import stoic_tutor
from existentialist import existentialist
from end_agent import end_agent

def choose_philosophy(state):
    input = state["messages"][-1].content
    philosophy = state["philosopher"]

    while end_agent(state) == "Continue":
        if philosophy == "eastern_guru":
            state = eastern_guru(state)
        elif philosophy == "stoic_tutor":
            state = stoic_tutor(state)
        elif philosophy == "existentialist":
            state = existentialist(state)
        else:
            print("ERROR: Invalid philosophy.")

    return state
