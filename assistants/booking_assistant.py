from apis.booking_api import BookingAPI
from faker import Faker
fake = Faker()

class BookingAssistant:
    def __init__(self, client, token):
        self.api = BookingAPI(client, token)

    def create_default_booking(self):
        payload = {
            "firstname": fake.first_name(),
            "lastname": fake.last_name(),
            "totalprice": fake.random_int(min=50, max=500),
            "depositpaid": fake.boolean(),
            "bookingdates": {
                "checkin": "2024-12-01",
                "checkout": "2024-12-05"
            },
            "additionalneeds": "Breakfast"
     }
        response = self.api.create_booking(payload)
        return response, payload

    def get_booking(self, booking_id):
        response = self.api.get_booking(booking_id)
        return response
