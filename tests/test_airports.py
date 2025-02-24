import logging
from typing import List, Tuple
from utils import get_airport_data
from api import AirportAPI
import pytest
from requests import Response, RequestException

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def test_get_all_airports() -> None:
    """Verify that we can retrieve all airports"""
    try:
        response: Response = AirportAPI.get_all_airports()
        assert response.status_code == 200, f"Expected 200 OK, got {response.status_code}"
    except RequestException as e:
        logger.error(f"API request failed: {e}")
        assert False, "API request failed"

# Load test data from airport_data.json
airport_data = get_airport_data().get("data", [])

# Extract valid test cases (ID and expected airport name)
airport_test_cases: List[Tuple[str, str]] = [
    (a["id"], a["attributes"]["name"]) for a in airport_data if "id" in a and "attributes" in a
]

@pytest.mark.parametrize("airport_id, expected_name", airport_test_cases)
def test_get_airport_by_id(airport_id: str, expected_name: str) -> None:
    """Verify that we can retrieve an airport using the ID from airport_data.json."""
    try:
        response: Response = AirportAPI.get_airport_by_id(airport_id)

        # Validate HTTP response
        assert response.status_code == 200, f"Expected 200 OK, got {response.status_code}"

        # Parse JSON response
        json_data = response.json()

        # Validate response structure
        assert "data" in json_data, "Response should contain 'data' field"
        assert json_data["data"]["id"] == airport_id, f"Expected airport ID {airport_id}, got {json_data['data']['id']}"
        assert json_data["data"]["attributes"]["name"] == expected_name, (
            f"Expected airport name {expected_name}, got {json_data['data']['attributes']['name']}"
        )

    except RequestException as e:
        logger.error(f"API request failed for airport ID {airport_id}: {e}")
        assert False, f"API request failed for {airport_id}"

    except KeyError as e:
        logger.error(f"Missing key in API response for {airport_id}: {e}")
        assert False, f"Missing expected data in response for {airport_id}"
