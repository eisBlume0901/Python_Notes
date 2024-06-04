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

gdpFile = pd.read_csv('gdp.csv')
recessionStatusFile = pd.read_csv('recession_status.csv')

gdp = pd.DataFrame(gdpFile)
recession_status = pd.DataFrame(recessionStatusFile)

gdp["date"] = pd.to_datetime(gdp["date"])
recession_status["date"] = pd.to_datetime(recession_status["date"])

gdp_recession_status = pd.merge_asof(gdp, recession_status, on="date")
is_recession = ['b' if s=="recession" else "y" for s in gdp_recession_status["econ_status"]]
gdp_recession_status.plot(kind="bar", y="gdp", x="date", color=is_recession, rot=90)
plt.tight_layout()
plt.show()