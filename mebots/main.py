import requests


class Instance:
    def __init__(self, raw):
        self.id = raw["id"]
        self.token = raw.get("token")

    def __repr__(self):
        return "<" + self.__class__.__name__ + ":" + self.id + ">"


class Bot:
    _HOST = "https://mebots.io"
    _API_ROOT = "/api/"

    def __init__(self, slug: str, token: str):
        self.slug = slug
        self.token = token

    def get(self, endpoint: str, params: dict = {}):
        """
        Make a GET request to the API.

        :param params: dictionary of custom params to add to request.
        """
        params.update({
            "token": self.token,
        })
        request = requests.get(self._HOST + self._API_ROOT + endpoint,
                               params=params)
        if request.ok:
            return request.json()
        else:
            raise Exception("API request failed. Received:\n" + request.text)

    def instances(self):
        return [Instance(raw) for raw in self.get(f"bots/{self.slug}/instances")]

    def instance(self, group_id: int):
        """
        Given a group ID, get the ID of the bot (instance) in that group.
        """
        return Instance(self.get(f"bots/{self.slug}/instances/{group_id}"))
