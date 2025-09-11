from enum import Enum


# https://github.com/LixxRarin/Clover.Space/blob/main/cloverspace/enum/
# https://github.com/D4rkwat3r/ProjZ/tree/main/projz/enum

class EAuthType(Enum):
    EMAIL = 1
    PHONE_NUMBER = 2

class EAuthPurpose(Enum):
    RENEW_SID = 0
    LOGIN = 1
    CHANGE_EMAIL = 3
    CHANGE_PHONE_NUMBER = 4
    ACTIVATE_WALLET = 5
    RECOVERY_PAYMENT_PASSWORD = 7
