from typing import Optional, Literal
from pydantic import BaseModel, Field, model_validator

class LoginDataModel(BaseModel):
    password: str
    authType: int
    purpose: int

    email: Optional[str] = None
    phoneNumber: Optional[str] = Field(None, alias="phoneNumber")

    @model_validator(mode="after")
    def check_email_or_phone(self):
        if bool(self.email) == bool(self.phoneNumber):
            # se os dois existem OU os dois são None → erro
            raise ValueError("Informe somente email ou somente phoneNumber (não ambos).")
        return self

