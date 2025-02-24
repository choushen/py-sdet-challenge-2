from utils import get_environment_data


class AuthAPI:
    """A class to handle authentication API calls."""

    @staticmethod
    def get_headers(self) -> dict:
        """Get the headers for the authentication token."""
        return {"Authorization": f"Bearer {self.get_token()}"}