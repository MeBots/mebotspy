import requests


class Bot:
    _HOST = "http://localhost:5000"
    _API_ROOT = "/api/"

    def __init__(self, slug: str, token: str):
        self.slug = slug
        self.token = token

    def get(self, params: dict = {}):
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

    def get_instance(self, group_id: int) -> str:
        """
        Given a group ID, get the ID of the bot (instance) in that group.
        """
        return self.get(f"bot/{self.slug}/{group_id}")
