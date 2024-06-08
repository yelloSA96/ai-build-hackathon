import sys
import os
from dotenv import load_dotenv

load_dotenv(".env")

PROJECT_DIRECTORY = os.getenv("PROJECT_DIRECTORY")
sys.path.insert(1, PROJECT_DIRECTORY)

from choose_philosophy import choose_philosophy
from eastern_guru import eastern_guru
#from stoic import stoic
#from existentialist import existentialist
from diagnostician import diagnostician
from prescriber import prescriber
from happiness import happy_agent

phil_response = choose_philosophy("My foot hurts.", "eastern_guru")
print("### philosophy response: ", phil_response)
happy_score = happy_agent(phil_response)
print("\n### happy score: ", happy_score)
diagnosis = diagnostician(phil_response)
print("\n### diagnosis: ", diagnosis)
prescription = prescriber(diagnosis)
print("\n### prescription: ", prescription)

