from typing List

from pydantic import BaseModel, validator
from datetime import date

class case_sensitive(BaseModel):
    values: List[]

    @validator('values')
    def check_values(cls, ):