"""Function for choosing a philosophy for the human to interact with."""

def choose_philosophy(input: str, philosophy: str):
    if philosophy == "eastern_guru":
        eastern_guru(input)
    elif philosophy == "stoic":
        stoic(input)
    elif philosophy == "existentialist":
        existentialist(input)
    else:
        print("ERROR: Invalid philosophy.")

    return
