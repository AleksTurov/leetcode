import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return products.loc[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y'), ['product_id']]

products = pd.DataFrame({
    'product_id': [1, 2, 3, 4, 5],
    'low_fats': ['Y', 'N', 'Y', 'N', 'Y'],
    'recyclable': ['Y', 'N', 'Y', 'N', 'N']
})
print(find_products(products))