import requests
from .base import AbstractMessanger


class EitaaMessanger(AbstractMessanger):
    def __init__(self):
        self.token = self.get_token('eitaa') 
        self.url = "https://eitaayar.ir/api/{token}/sendMessage".format(token=self.token)
    
    def send_message(self, text, receiver):
        data = {
            'chat_id' : receiver,
            'text' : text,
        }
         
        res =requests.post(self.url, data=data)
        return res.json()