from pydantic import BaseModel
from datetime import datetime

class TransactionIn(BaseModel):
   
    value: int username: str

class TransactionOut(BaseModel):
    id_transaction: int
    username: str
    date: datetime
    value: int
    actual_balance: int