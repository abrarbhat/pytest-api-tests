from jsonschema import validate
from schemas.booking_schema import booking_schema  # assuming booking_schema is a dict
from deepdiff import DeepDiff

def test_create_booking(booking_assistant):
    response, expected_payload = booking_assistant.create_default_booking()
    assert response.status_code == 200

    data = response.json()
    assert "bookingid" in data
    booking = data["booking"]
    validate(instance=data, schema=booking_schema)

    diff = DeepDiff(booking, expected_payload, ignore_order=True)
    assert diff == {}, f"Differences found: {diff}"

def test_get_booking(booking_assistant):
    create_response, expected_payload = booking_assistant.create_default_booking()

    booking_id = create_response.json()["bookingid"]

    get_response = booking_assistant.get_booking(booking_id)
    assert get_response.status_code == 200
    data = get_response.json()
    assert "bookingid" not in data
    
    assert get_response.json()["firstname"] == expected_payload.get("firstname")
    diff = DeepDiff(data, expected_payload, ignore_order=True)
    assert diff == {}, f"Differences found: {diff}"
