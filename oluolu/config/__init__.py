from typing import Optional

from ..models.enum.auth import EAuthType, EAuthPurpose
from ..headers import Headers

class AccountBase:
    def __init__(self, email: Optional[str] = None, number: Optional[str] = None, password: Optional[str] = None, authType: Optional[int] = None) -> None:

        self.email = email
        self.number = number
        self.authType = authType
        self.purpose = EAuthPurpose.RENEW_SID.value

        self.__password = password
        self.headers: Headers = Headers()

    def GetPassword(self) -> Optional[str]:
        return self.__password

class AccEmail(AccountBase):
    def __init__(self, email: str, password: str) -> None:
        super().__init__(email=email, password=password, authType=EAuthType.EMAIL.value)

class AccNumber(AccountBase):
    def __init__(self, number: str, password: str) -> None:
        super().__init__(number=number, password=password, authType=EAuthType.PHONE_NUMBER.value)

