from pydantic import BaseModel
from typing import List


class RequestModel(BaseModel):
    iso: str
    countries: List[str]

class RespModel(BaseModel):
    iso: str
    match_count: int
    matches: List[str]
