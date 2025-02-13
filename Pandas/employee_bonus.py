import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    merge_df = employee.merge(bonus, on='empId', how='left')
    return merge_df[((merge_df['bonus'].isnull()) | (merge_df['bonus'] < 1000))][['name', 'bonus']]

# Test Cases
employee = pd.DataFrame({
    'empId': [1, 2, 3, 4, 5],
    'name': ['John', 'Alice', 'Bob', 'Dylan', 'Cathy']
})
bonus = pd.DataFrame({
    'empId': [1, 2, 3, 4],
    'bonus': [1000, 2000, 3000, 4000]
})
print(employee_bonus(employee, bonus))
