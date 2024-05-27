import pandas as pd

customersFile = pd.read_csv('customers.csv')
ordersFile = pd.read_csv('orders.csv')

customers = pd.DataFrame(customersFile)
orders = pd.DataFrame(ordersFile)

pd.set_option('display.max_columns', None)  # None means unlimited
pd.set_option('display.expand_frame_repr', False)  # Don't wrap to multiple pages
pd.set_option('display.max_rows', None)  # None means unlimited

customers_orders = customers.merge(orders, how="outer", on="customer_id", suffixes=("_c", "_o"))
print(customers_orders)

print("Customers that does not have any orders")
print(customers_orders[customers_orders["product"].isnull()]["customer_name"])