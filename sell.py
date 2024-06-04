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
        # Check if the balance is greater than 10 DAI
        balance = get_available_dai()
        if balance >= batch:
            # Create a sell order for 10 DAI at 1.0001 USDT per DAI
            create_sell_order()
        else:
            print("Insufficient balance. Current balance: {0:.2f} DAI".format(balance))
    except Exception as e:
        print(f"An error occurred: {e}")

def get_available_dai():
    coin = session.get_wallet_balance(
        accountType="UNIFIED",
        coin="DAI",
    )['result']['list'][0]['coin'][0]
    total = float(coin['walletBalance'])
    locked = float(coin['locked'])
    available = total - locked
    # print(available)
    return float(available)

def create_sell_order():
    order = session.place_order(
        category="spot",
        symbol="DAIUSDT",
        side="Sell",
        orderType="Limit",
        qty=batch,
        price=1.0001,
        time_in_force="GoodTillCancel"
    )
    print("Order placed:", order)
    return order

# Execute the strategy every 3 seconds
while True:
    # get_available_dai()
    execute_strategy()
    time.sleep(3)
