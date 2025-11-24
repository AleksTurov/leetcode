import pandas as pd

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    '''
    Write a solution to get the names of products that have at least 100 units ordered in February 2020 and their amount.
    Return the result table in any order.
    The result format is in the following example.
    '''
    orders = orders.query('order_date >= "2020-02-01" and order_date < "2020-03-01"')
    orders = orders.groupby('product_id')['unit'].sum().reset_index()
    orders = orders.query('unit >= 100')
    products = products.merge(orders, on='product_id', how='inner')
    return products[['product_name', 'unit']]

# Example usage:
products = pd.DataFrame({
    'product_id': [1, 2, 3, 4],
    'product_name': ['Product A', 'Product B', 'Product C', 'Product D']
})  
orders = pd.DataFrame({
    'order_id': [101, 102, 103, 104, 105, 106],
    'product_id': [1, 2, 1, 3, 2, 4],
    'unit': [50, 60, 70, 30, 50, 20],
    'order_date': pd.to_datetime([
        '2020-02-05', '2020-02-15', '2020-02-20', 
        '2020-01-25', '2020-02-28', '2020-03-01'
    ])
})
result = list_products(products, orders)
print(result)