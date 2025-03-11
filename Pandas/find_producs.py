import pandas as pd

def find_valid_serial_products(products: pd.DataFrame) -> pd.DataFrame:
    valid_serials = products[products['description'].str.contains(r'\bSN\d{4}-\d{4}\b')]
    return valid_serials.sort_values(by='product_id')


    