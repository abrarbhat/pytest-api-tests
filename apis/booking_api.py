from utils.logger import get_logger

logger = get_logger(__name__)

class BookingAPI:
    def __init__(self, client, token=None):
        self.client = client
        self.token = token

    def create_booking(self, payload):
        logger.info("Creating booking with payload: %s", payload)
        response = self.client.post("/booking", json=payload)
        logger.info("Received response: %s", response.json())
        return response

    def get_booking(self, booking_id):
        return self.client.get(f"/booking/{booking_id}")

    def delete_booking(self, booking_id):
        headers = {"Cookie": f"token={self.token}"}
        return self.client.delete(f"/booking/{booking_id}", headers=headers)
