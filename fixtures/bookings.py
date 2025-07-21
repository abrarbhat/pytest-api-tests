# import pytest
# from apis.booking_api import BookingAPI

# @pytest.fixture
# def booking_api(client, auth_token):
#     return BookingAPI(client, auth_token)

import pytest
from assistants.booking_assistant import BookingAssistant

@pytest.fixture
def booking_assistant(client, auth_token):
    return BookingAssistant(client, auth_token)