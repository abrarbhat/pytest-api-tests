import pytest
import yaml
from utils.api_client import APIClient
from fixtures.auth import auth_token
from fixtures.bookings import booking_assistant  # ✅ This line is essential

@pytest.fixture(scope="session")
def config():
    with open("configs/config.yaml") as f:
        return yaml.safe_load(f)

@pytest.fixture(scope="session")
def client(config):
    return APIClient(config['base_url'])