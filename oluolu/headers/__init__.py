from typing import Optional

import hashlib
import hmac
import base64
import uuid
import time
from typing import Dict, Optional

class Headers():
    def __init__(
            self,
            accept_language: str = "pt-BR",
            country_code: str = "BR",
            time_zone: int = -180,
            carrierCountryCodes: str = "br,",
            contentLanguages: str = "pt",
            timeZoneId: str = "America/Sao_Paulo"

    ) -> None:
        self.__keys = ["rawDeviceId", "rawDeviceIdTwo", "rawDeviceIdThree", "appType", "appVersion", "osType", "deviceType", "sId", "countryCode", "reqTime", "User-Agent", "contentRegion", "nonce", "carrierCountryCodes",]
        self.__installation_id = str(uuid.uuid4())

        self.__sid: Optional[str] = None        
        self.__deviceId: str = ((lambda prefix, final_hash: (prefix + final_hash).hex())(bytes([0x04]) + hashlib.sha1(self.__installation_id.encode()).digest(), hashlib.sha1((bytes([0x04]) + hashlib.sha1(self.__installation_id.encode()).digest()) +hashlib.sha1(bytes.fromhex("997ec928a85f539e3fa124761e7572ef852e")).digest()).digest()))

        self.__headers = {
            "appType": "OluOluApp",
            "appPlatform": "3",
            "appVersion": "0.12.5",
            "osType": "5",
            "deviceType": "1",
            "Accept-Language": accept_language,
            "countryCode": country_code,
            "timeZone": time_zone,
            "carrierCountryCodes": carrierCountryCodes,
            "contentLanguages": contentLanguages,
            "timeZoneId": timeZoneId,
            "flavor": "download",
            "Accept-Encoding": "gzip",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
            "deviceId": self.__deviceId
        }

    def SetSid(self, sid) -> None:
        self.__sid = sid
    
    def GetSid(self) -> str:
        return self.__sid

    def GetHeaders(self) -> dict:
        self.__headers["reqTime"] = str(int(time.time() * 1000))
        self.__headers["nonce"] = str(uuid.uuid4())

        return self.__headers