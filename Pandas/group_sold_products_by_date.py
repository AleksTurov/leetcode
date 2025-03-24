import pandas as pd

# Create a dictionary with the data
data = {
    'sell_date': ['2020-05-30', '2020-06-01', '2020-06-02', '2020-05-30', '2020-06-01', '2020-06-02', '2020-05-30'],
    'product': ['Headphone', 'Pencil', 'Mask', 'Basketball', 'Bible', 'Mask', 'T-Shirt']
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

import pandas as pd
# Remove duplicate products for each sell_date

def group_sold_products_by_date(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates(subset=['sell_date', 'product'])
    grouped = df.groupby('sell_date').agg(
        num_sold=('product', 'size'),
        products=('product', lambda x: ','.join(sorted(x)))
    ).reset_index()
    return grouped

print(group_sold_products_by_date(df))
