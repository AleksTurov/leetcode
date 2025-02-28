import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return pd.melt(report, id_vars=['product'], var_name='quarter', value_name='sales')

# Create a sample DataFrame
data = {
    'product': ['A', 'B', 'C'],
    'quarter_1': [100, 150, 200],
    'quarter_2': [120, 160, 210],
    'quarter_3': [130, 170, 220],
    'quarter_4': [140, 180, 230]
}   
report = pd.DataFrame(data)
print(meltTable(report))
