import json
from abc import ABC, abstractmethod


class AbstractMessanger(ABC):
    def get_token(self, messanger):
        with open('messanger/tokens.json') as file:
            token = json.load(file)[messanger]

        return token

    @abstractmethod
    def send_message(self, text, receiver):
        pass