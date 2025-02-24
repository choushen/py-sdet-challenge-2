import requests
from requests.models import Response
from utils import get_environment_data


class AirportAPI:
    """A class to handle airport API calls."""

    @staticmethod
    def get_all_airports() -> Response:
        """Get all airports from the API."""
        url: str = f"{get_environment_data()['base_url']}/airports"
        response = requests.get(url)
        return response