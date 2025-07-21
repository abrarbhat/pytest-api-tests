# fixtures/auth.py
import pytest
from apis.auth_api import AuthAPI

@pytest.fixture(scope="session")
def auth_token(client, config):
    api = AuthAPI(client)
    response = api.get_token(config["username"], config["password"])
    return response
