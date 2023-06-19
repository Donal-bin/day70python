import requests
response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
response.raise_for_status()


class Post:
    def __init__(self):
        self.data = {}

    def create_post(self):
        self.data = response.json()
        return self.data
