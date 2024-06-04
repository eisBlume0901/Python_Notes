import pandas as pd
import matplotlib.pyplot as plt

stockPriceCompanyA = pd.read_csv('stock_price_companyA.csv')
stockPriceCompanyB = pd.read_csv('stock_price_companyB.csv')
stockPriceCompanyC = pd.read_csv('stock_price_companyC.csv')

stock_a = pd.DataFrame(stockPriceCompanyA)
stock_b = pd.DataFrame(stockPriceCompanyB)
stock_c = pd.DataFrame(stockPriceCompanyC)

stock_a["date_time"] = pd.to_datetime(stock_a["date_time"])
stock_b["date_time"] = pd.to_datetime(stock_b["date_time"])
stock_c["date_time"] = pd.to_datetime(stock_c["date_time"])


stock_a_b = pd.merge_asof(stock_a, stock_b, on="date_time",  direction="nearest", suffixes=("", "_b"))
stock_a_b_c = pd.merge_asof(stock_a_b, stock_c, on="date_time", suffixes=("_a", "_c"), direction="nearest")
print(stock_a_b_c)

price_diffs = stock_a_b_c.diff()
print(price_diffs)

price_diffs.plot(y=["price_a", "price_b", "price_c"])
plt.show()

