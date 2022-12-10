import json
from abc import ABC, abstractmethod


class AbstractMessanger(ABC):
    def get_token(self, key):
        with open('messanger/secret.json') as secret_file:
            token = json.load(secret_file)[key]

        return token

    @abstractmethod
    def send_message(self, text, receiver):
        pass