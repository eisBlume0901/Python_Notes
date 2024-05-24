import pandas as pd

shoemakersFile = pd.read_csv('shoemakers.csv')
ordersFile = pd.read_csv('orders.csv')
customersFile = pd.read_csv('customers.csv')

shoemakers = pd.DataFrame(shoemakersFile)
orders = pd.DataFrame(ordersFile)
customers = pd.DataFrame(customersFile)

pd.set_option('display.max_columns', None)  # None means unlimited
pd.set_option('display.expand_frame_repr', False)  # Don't wrap to multiple pages
pd.set_option('display.max_rows', None)  # None means unlimited

shoemakers_orders_customers = shoemakers.merge(orders, on="product").merge(customers, on="customer_id")

print(shoemakers_orders_customers)

filterCriteria = (shoemakers_orders_customers['product'] == 'Chuck Taylor Shoes')

print("Total Number of Chuck Taylor Shoes ordered")
# Reminder: filterCritera is row, quantity is column (goal: to find a specific cell)
print(shoemakers_orders_customers.loc[filterCriteria, 'quantity'].sum())

