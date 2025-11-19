from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from BankWallet import Wallet, InsufficientFundsError

app = FastAPI()

my_wallet = Wallet("Admin", "USD")

class Transaction(BaseModel):
    amount: float

@app.get("/balance")
def get_balance():
    return {
        "name": my_wallet.name,
        "balance": my_wallet.balance,
        "currency": my_wallet.currency
    }

@app.post("/deposit")
def make_deposit(transaction: Transaction):
    try:
        my_wallet.deposit(transaction.amount)
        return {"status": "success", "new_balance": my_wallet.balance}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/withdraw")
def make_withdraw(transaction: Transaction):
    try:
        my_wallet.withdraw(transaction.amount)
        return {"status": "success", "new_balance": my_wallet.balance}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except InsufficientFundsError as e:
        raise HTTPException(status_code=400, detail=str(e))