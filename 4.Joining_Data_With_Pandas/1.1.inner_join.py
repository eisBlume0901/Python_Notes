import pandas as pd

customersFile = pd.read_csv('customers.csv')
ordersFile = pd.read_csv('orders.csv')

customers = pd.DataFrame(customersFile)
orders = pd.DataFrame(ordersFile)


print(customers.shape)
print(customers.columns)
print(orders.shape)
print(orders.columns)

customers_orders = customers.merge(orders, on="customer_id")
# adding suffixes parameter (left_indicator, right_indicator) if there are column names that has the same name
# example: customers_orders = customers.merge(orders, on="customer_id", suffixes=('_c', '_o')

print(customers_orders)
