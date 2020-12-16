from fastapi import Depends,FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware

from routers.user_router import router as router_users
from routers.transaction_router import router as router_transactions

api =FastAPI()

api.include_router(router_users)
api.include_router(router_transactions)

import datetime

origins =[
    "http://localhost.tiangolo.com","https://localhost.tiangolo.com",
    "https://localhost", "http://localhost:8080","http://localhost:5432", "https://cajero-app1912.herokuapp.com"
]

api.add_middleware(
    CORSMiddleware, allow_origins=origins,
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

# @api.post("/user/auth/")
# async def auth_user(user_in: UserIn):
    
#     user_in_db = get_user(user_in.username)
    
#     if user_in_db == None:
#         raise HTTPException(status_code=404, detail="El usuario no existe")

#     if user_in_db.password != user_in.password:
#         raise HTTPException(status_code=403, detail="Error de autenticación")
        
#         return {"Autenticado": False}
#     return {"Autenticado": True}


# @api.get("/user/balance/{username}")
# async def get_balance(username: str):
    
#     user_in_db = get_user(username)

#     if user_in_db == None:
#         raise HTTPException(status_code=404,detail="El usuario no existe")

#     user_out = UserOut(**user_in_db.dict())
#     return user_out

# @api.put("/user/transaction/")
# async def make_transaction(transaction_in: TransactionIn):

#     user_in_db = get_user(transaction_in.username)

#     if user_in_db == None:
#         raise HTTPException(status_code=404,detail="El usuario no existe")

#     if user_in_db.balance < transaction_in.value:
#         raise HTTPException(status_code=400,detail="Sin fondos suficientes")

#     user_in_db.balance = user_in_db.balance - transaction_in.value
#     update_user(user_in_db)
#     transaction_in_db = TransactionInDB(**transaction_in.dict(),actual_balance = user_in_db.balance)
#     transaction_in_db = save_transaction(transaction_in_db)
#     transaction_out = TransactionOut(**transaction_in_db.dict())
#     return transaction_out