from pybit.unified_trading import HTTP
import time

# Setup Bybit API
session = HTTP(
    testnet=False,
    api_key="",
    api_secret="",
)

# variables
batch = 10.0

# Function to check balance and create order
def execute_strategy():
    try:
        # Check if the balance is greater than 10 USDT
        balance = get_available_usdt()
        if balance >= batch:
            # Create a buy order for 10 DAI at 1.0000 USDT per DAI
            create_buy_order()
        else:
            print("Insufficient balance. Current balance: {0:.2f} USDT".format(balance))
    except Exception as e:
        print(f"An error occurred: {e}")

def get_available_usdt():
    coin = session.get_wallet_balance(
        accountType="UNIFIED",
        coin="USDT",
    )['result']['list'][0]['coin'][0]
    total = float(coin['walletBalance'])
    locked = float(coin['locked'])
    available = total - locked
    # print(available)
    return float(available)

def create_buy_order():
    order = session.place_order(
        category="spot",
        symbol="DAIUSDT",
        side="Buy",
        orderType="Limit",
        qty=batch,
        price=1.0000,
        time_in_force="GoodTillCancel"
    )
    print("Order placed:", order)
    return order

# Execute the strategy every 3 seconds
while True:
    # get_available_usdt()
    execute_strategy()
    time.sleep(3)
