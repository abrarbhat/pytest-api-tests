# apis/auth_api.py
class AuthAPI:
    def __init__(self, client):
        self.client = client

    def get_token(self, username, password):
        payload = {
            "username": username,
            "password": password
        }
        response = self.client.post("/auth", json=payload)
        token = response.json().get("token")
        return token
