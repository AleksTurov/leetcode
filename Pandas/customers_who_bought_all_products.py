import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    product_count = customer.groupby('customer_id')['product_key'].nunique().reset_index()
    return product_count[product_count['product_key'] == len(product)][['customer_id']]
