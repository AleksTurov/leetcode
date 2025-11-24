import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    '''
    Write a solution to report the products that were only sold in the first quarter of 2019. That is, between 2019-01-01 and 2019-03-31 inclusive.
    Return the result table in any order.
    The result format is in the following example.
    '''
    sales_ids = sales.query('sale_date < "2019-01-01" or sale_date > "2019-03-31"')['product_id'].unique()
    sales_ids_beetween = sales[~sales['product_id'].isin(sales_ids)]['product_id'].unique()
    return product[product['product_id'].isin(sales_ids_beetween)][['product_id', 'product_name']]
    
# Example usage:
product = pd.DataFrame({
    'product_id': [1, 2, 3, 4],
    'product_name': ['Product A', 'Product B', 'Product C', 'Product D']
})  
sales = pd.DataFrame({
    'sale_id': [101, 102, 103, 104, 105, 106],
    'product_id': [1, 2, 1, 3, 2, 4],
    'sale_date': ['2019-01-15', '2019-02-20', '2019-04-10', '2019-03-05', '2019-05-25', '2019-02-28']   
})
sales['sale_date'] = pd.to_datetime(sales['sale_date']) 
result = sales_analysis(product, sales)
print(result) # Expected output: DataFrame with products sold only in Q1 2019
