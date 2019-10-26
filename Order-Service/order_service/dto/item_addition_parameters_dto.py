from pydantic import BaseModel


class ItemAdditionParametersDto(BaseModel):
    id: int
    amount: int
    username: str
