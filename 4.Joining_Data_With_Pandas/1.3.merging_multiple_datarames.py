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

# Reminder: groupby allows you to categorize data through a specific column variable and get their descriptive statistics.
print("Total Number of Orders for Each Shoes")
print(shoemakers_orders_customers.groupby("product", as_index=False).agg({"quantity": "sum"}))
# grouped = df.groupby(['column1', 'column2'], as_index=False).agg({'column3':'sum'})
# as_index means the group labels are not set as index, they remain as columns and their default integer index is used