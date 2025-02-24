import os
import requests
from utils import get_environment_data

def test_get_all_airports():
    """Verify that the /airports endpoint returns a list of airports"""
    response = requests.get(f"{get_environment_data()["base_url"]}/airports")
    assert response.status_code == 200, "Expected 200 OK"