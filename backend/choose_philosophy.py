"""Function for choosing a philosophy for the human to interact with."""
import sys
import os
from dotenv import load_dotenv

load_dotenv(".env")

PROJECT_DIRECTORY = os.getenv("PROJECT_DIRECTORY")
sys.path.insert(1, PROJECT_DIRECTORY)

from eastern_guru import eastern_guru
from stoic_tutor import stoic_tutor


def choose_philosophy(input: str, philosophy: str):
    if philosophy == "eastern_guru":
        response = eastern_guru(input)
    elif philosophy == "stoic_tutor":
        response = stoic_tutor(input)
    elif philosophy == "existentialist":
        response = existentialist(input)
    else:
        print("ERROR: Invalid philosophy.")

    return response
