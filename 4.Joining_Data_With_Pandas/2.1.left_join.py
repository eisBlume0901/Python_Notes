import pandas as pd

customersFile = pd.read_csv('customers.csv')
ordersFile = pd.read_csv('orders.csv')

customers = pd.DataFrame(customersFile)
orders = pd.DataFrame(ordersFile)

pd.set_option('display.max_columns', None)  # None means unlimited
pd.set_option('display.expand_frame_repr', False)  # Don't wrap to multiple pages
pd.set_option('display.max_rows', None)  # None means unlimited

print(customers.shape)
print(orders.shape)

customers_orders_left_join = customers.merge(orders, on="customer_id", how="left") # left table is customers
print(customers_orders_left_join.shape)

print(customers_orders_left_join)

print("Number of customers who did not buy anything")
print(customers_orders_left_join["order_id"].isnull().sum())
# .isnull() checks a data if its NaN

print(customers_orders_left_join.isna().sum()) # Checks which column entry is NaN or null and returns how many rows it is
# (review topic 3.Data_Manipulation_With_Pandas > 4.2.missing_values.py

print(customers_orders_left_join.isna().any().sum()) # Checks how many column entry is NaN or null

print(customers_orders_left_join.fillna(0)) # Replaces NaN with 0
