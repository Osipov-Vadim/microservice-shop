from pydantic import BaseModel


class OrderIdDto(BaseModel):
    id: int
