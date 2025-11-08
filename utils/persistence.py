import json
import os

DATA_FILE = os.path.join("data", "data.json")


def load_data():
    """
    Load data from the JSON file. 
    If the file is empty or missing, return an empty structure.
    """
    if not os.path.exists(DATA_FILE):
        return {"users": []}

    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            return data
    except json.JSONDecodeError:
        return {"users": []}


def save_data(data):
    """
    Save the given data dictionary back into the JSON file.
    """
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)
