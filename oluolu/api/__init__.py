from typing import Union
from ..config import AccEmail, AccNumber


class Req():
    def __init__(self, account: Union[AccEmail, AccNumber]):
        self.account = account

    def __request(self):
        pass

    def post(self, path: str, data: dict):
        print(path, data)

    def post_empty(self, path: str):
        print(path)
