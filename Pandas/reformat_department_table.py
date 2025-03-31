import pandas as pd

# Input data
data = {
    "id": [1, 2, 3, 1, 1],
    "revenue": [8000, 9000, 10000, 7000, 6000],
    "month": ["Jan", "Jan", "Feb", "Feb", "Mar"]
}

# Create DataFrame
df = pd.DataFrame(data)

print(df)

def reformat_table(department: pd.DataFrame) -> pd.DataFrame:
    # Pivot the table to have months as columns
    department = department.pivot(index='id', columns='month', values='revenue')
    
    all_months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    department = department.reindex(columns=all_months)
    
    department.columns = [f"{month}_Revenue" for month in department.columns]
    
    department = department.reset_index()
    
    return department

print(reformat_table(df))