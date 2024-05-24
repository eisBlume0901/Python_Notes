import pandas as pd

# one to one - every row in the left table is related to only one row in the right table
# examples: each person has one social security number, and each social security number is associated with
# one person

# one to many - every row in left table ot one or more rows in the right table
# examples: a customer can place many orders, but each order is associated with one customer

customersFile = pd.read_csv('customers.csv')
ordersFile = pd.read_csv('orders.csv')

customers = pd.DataFrame(customersFile)
orders = pd.DataFrame(ordersFile)

print(customers.shape)
print(orders.shape)

customers_orders = customers.merge(orders, on="customer_id", suffixes=('_c', '_o'))
print(customers_orders.shape)
print(customers_orders)

orders_by_customers = customers_orders.groupby(['customer_name', 'product']).agg({'quantity': 'sum'})
print(orders_by_customers)

sorted_orders_by_customers = orders_by_customers.sort_values('quantity', ascending=False)
print(sorted_orders_by_customers)