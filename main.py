from typing import Union
from fastapi import FastAPI
from pybit.unified_trading import HTTP
from pydantic import BaseModel

app = FastAPI()

class BybitAPI(BaseModel):
    api_key: str
    api_secret: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post('/trading-business/query-usdt-balance')
def query_usdt_balance(bybitapi: BybitAPI):
    session = HTTP(
        testnet=False,
        api_key=bybitapi.api_key,
        api_secret=bybitapi.api_secret,
    )
    coin = session.get_wallet_balance(
        accountType="UNIFIED",
        coin="USDT",
    )['result']['list'][0]['coin'][0]
    total = float(coin['walletBalance'])
    locked = float(coin['locked'])
    balance = total - locked
    return {'balance': balance}
