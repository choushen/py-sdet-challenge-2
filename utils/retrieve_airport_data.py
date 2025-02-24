import json
from typing import Dict, Any
from utils import get_airport_data

# Cache the data to avoid multiple calls
_airport_data: Dict[str, Any] | None = None  # Global variable for caching

def get_cached_airport_data() -> Dict[str, Any]:
    """Load airport data once and return cached data on subsequent calls."""
    global _airport_data  # Use global cache
    if _airport_data is None:
        _airport_data = get_airport_data()
    return _airport_data

def search_airport_by_id(airport_id: str) -> dict | None:
    """Find an airport by its ID."""
    data = get_cached_airport_data()  # Use cached data
    return next((airport for airport in data["data"] if airport["id"] == airport_id), None)

def search_airport_id_by_city(city_name: str) -> str | None:
    """Find the airport ID by city name (case-insensitive)."""
    data = get_cached_airport_data()  # Use cached data
    airport = next(
        (airport for airport in data["data"] if airport["attributes"]["city"].lower() == city_name.lower()),
        None
    )
    return airport["id"] if airport else None
