import requests
from .base import AbstractMessanger


class BaleMessanger(AbstractMessanger):
    def __init__(self):
        self.token = self.get_token("bale")
        self.url = "https://tapi.bale.ai/bot{token}/sendMessage".format(
            token=self.token,
        )

    def send_message(self, text, receiver):
        data = {
            "chat_id": receiver,
            "text": text,
        }

        res = requests.post(self.url, data=data)
        return res.json()
