import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint, params=None, headers=None):
        return requests.get(f"{self.base_url}{endpoint}", params=params, headers=headers)

    def post(self, endpoint, data=None, json=None, headers=None):
        return requests.post(f"{self.base_url}{endpoint}", data=data, json=json, headers=headers)

    def put(self, endpoint, data=None, json=None, headers=None):
        return requests.put(f"{self.base_url}{endpoint}", data=data, json=json, headers=headers)

    def delete(self, endpoint, headers=None):
        return requests.delete(f"{self.base_url}{endpoint}", headers=headers)
