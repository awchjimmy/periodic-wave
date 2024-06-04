# periodic-wave
Stablecoin arbitrage

### What is Stablecoin Arbitrage?
Stablecoin arbitrage involves finding stablecoin trading pairs, such as USDC/USDT or DAI/USDT. You buy at $1.0000 and sell at $1.0001, capturing a spread of $0.0001.

### Why Choose Stablecoins?
Stablecoins are preferred because their prices are designed to return to a 1:1 peg, minimizing the risk of significant price deviations that might not revert. This stability reduces risk, it also means lower returns, requiring time to accumulate meaningful profits.

### Transaction Fees?
Find trading pairs with low or zero transaction fees, so fees don't eat up your profits.

### What is the estimated APY?

1. Initial Funds: $10,000, earning $1 per arbitrage.
2. Arbitrage once per day, 365 times a year, earning $365.
3. Server operating costs: $60 per year.
4. Returns - costs: ($365 - $60) / $10,000 ≈ 3%.

### Why Not Choose Staking/Flexible Savings...?
Consider this: What if you could perform arbitrage multiple times a day? What if other financial products cease to offer high returns?

----

### Example Setup
```sh
# install virtual env
$ python -m venv venv

# install dependencies using pip
$ venv/bin/pip install -r requirements.txt

# fill in the bybit api keys
# buy.py
# sell.py

# run buy.py
$ venv/bin/python buy.py

# run sell.py
$ venv/bin/python sell.py

```

### Order History
[Order History](https://docs.google.com/spreadsheets/d/1CymlgyBs_0JJKBhThmBrkfnKz5ASsbHT3nMJgmzlN9w/edit?usp=sharing)
