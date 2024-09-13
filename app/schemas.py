from pydantic import BaseModel


class InputIrisData(BaseModel):
    sl: float = 5.8
    sw: float = 3.0
    pl: float = 4.35
    pw: float = 1.3


class OutputIrisData(BaseModel):
    species: int
