import requests
from utils import get_environment_data
from api import AirportAPI

def test_get_all_airports():
    """Verify that the /airports endpoint returns a list of airports"""
    response = AirportAPI.get_all_airports()
    assert response.status_code == 200, "Expected 200 OK"