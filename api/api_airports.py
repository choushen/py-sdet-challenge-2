import requests
from requests.models import Response
from utils import get_environment_data, get_endpoints_data


class AirportAPI:
    """A class to handle airport API calls."""


    @staticmethod
    def get_all_airports() -> Response:
        """Get all airports from the API."""
        endpoint: str = get_endpoints_data()["airports"]["all_airports"]
        url: str = f"{get_environment_data()['base_url']}{endpoint}"
        response = requests.get(url)
        return response
    
    @staticmethod
    def get_airport_by_id(airport_id: str) -> Response:
        """Get an airport by its ID."""
        endpoint: str = get_endpoints_data()["airports"]["airport_by_id"]
        final_endpoint: str = endpoint.replace("{id}", airport_id)
        url: str = f"{get_environment_data()['base_url']}{final_endpoint}"
        response = requests.get(url)
        return response