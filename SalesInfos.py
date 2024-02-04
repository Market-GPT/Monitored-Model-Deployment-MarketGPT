from pydantic import BaseModel
from datetime import date
from typing import List

class SalesInfo(BaseModel):
    lag_1: List[float]
    lag_2: List[float]
    lag_3: List[float]
    lag_4: List[float]
    lag_5: List[float]
    

