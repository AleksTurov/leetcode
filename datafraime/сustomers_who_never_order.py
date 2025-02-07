import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    customers_name = customers[~customers['id'].isin(orders['customerId'])]['name']
    return customers_name.to_frame(name='Customers')
    
customers = pd.DataFrame({'id': [1, 2, 3, 4], 'name': ['Joe', 'Henry', 'Sam', 'Max']})
orders = pd.DataFrame({'id': [1, 2], 'customerId': [3, 1]})
print(find_customers(customers, orders))
