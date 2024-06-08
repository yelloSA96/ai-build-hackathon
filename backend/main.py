import os, sys
from dotenv import load_dotenv

load_dotenv(".env")

PROJECT_DIRECTORY = os.getenv("PROJECT_DIRECTORY")
sys.path.insert(1, PROJECT_DIRECTORY)

from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

from langchain_core.messages import HumanMessage
from choose_philosophy import choose_philosophy
from eastern_guru import eastern_guru
from stoic_tutor import stoic_tutor
from existentialist import existentialist
from diagnostician import diagnostician
from prescriber import prescriber
from happiness import happy_agent


@app.route('/api', methods=["POST"])
def getting_ai_response():
    data = request.json
    print(data)
    human_query = data.get('human_query')
    prompt = HumanMessage(content=human_query, name="human")
    philosopher = data.get('philosopher')

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

    last_message = state["messages"][-1].content
    happiness_score = state["happiness_score"]

    print("\n### prescription: ", state)
    data = { 
            "happiness_score" : happiness_score,
            "last_message" :last_message
        } 
    return jsonify(data), 201


if __name__ == '__main__':
    app.run(debug=True, port=8080)
