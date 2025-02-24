import json, os
from dotenv import load_dotenv
from typing import Dict, Any


def read_json(file_path: str) -> Dict[str, Any]:
    """ Read a JSON file and return a dictionary """
    with open(file_path, "r") as file:
        return json.load(file)
    

def get_endpoints() -> Dict[str, Any]:
    """ Get the checkout data from the JSON file """
    file_path: str = os.path.join(os.path.dirname(os.path.dirname(__file__)), "resources", "api_endpoints")
    return read_json(file_path)


def get_favourites() -> Dict[str, Any]:
    """ Get the test validation data from the JSON file """
    file_path: str = os.path.join(os.path.dirname(os.path.dirname(__file__)), "resources", "favourites.json")
    return read_json(file_path)


def get_environment_data() -> Dict[str, Any]:
    """ Get the environment data from the .env file """
    # Load .env from the project root
    load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"))
    env_dict: Dict[str, Any] = {
        "base_url": os.getenv("BASE_URL"),
        "auth_token": os.getenv("AUTH_TOKEN"),
    }
    return env_dict

