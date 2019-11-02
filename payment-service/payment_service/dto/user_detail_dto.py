import enum
from pydantic import BaseModel


class CardAuthorizationInfo(enum.Enum):
    AUTHORIZED = "AUTHORIZED"
    UNAUTHORIZED = "UNAUTHORIZED"


class UserDetailsDto(BaseModel):
    username: str
    cardAuthorizationInfo: CardAuthorizationInfo
