import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    # Use pd.melt to convert wide table to long format
    df = pd.melt(products, id_vars=['product_id'], var_name='store', value_name='price')
    
    # Remove rows with null prices
    df = df.dropna()
    
    # Reset index for clean output
    df = df.reset_index(drop=True)
    
    return df

# Example usage
products = pd.DataFrame({
    'product_id': [1, 2],
    'store_1': [100, 200],
    'store_2': [150, 250],
    'store_3': [120, 220]
})
print(rearrange_products_table(products))
