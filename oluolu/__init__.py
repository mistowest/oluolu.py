from typing import Optional, Union

from .config import AccNumber, AccEmail
from .models.base.auth import LoginDataModel
from .api import Req

class Client():
    def __init__(self, account: Union[AccEmail, AccNumber]) -> None:
        self.account: Union[AccEmail, AccNumber] = account
        self.request: Req = Req(self.account)