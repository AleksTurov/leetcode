import pandas as pd

# Create the Salary table with correct formats
data = {
    'id': pd.Series([1, 2, 3, 4], dtype='int'),
    'name': pd.Series(['A', 'B', 'C', 'D'], dtype='string'),
    'sex': pd.Categorical(['m', 'f', 'm', 'f']),
    'salary': pd.Series([2500, 1500, 5500, 500], dtype='int')
}
salary_df = pd.DataFrame(data)

#def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
#    salary['sex'] = salary['sex'].map({'m': 'f', 'f': 'm'})
#    #salary['sex'].apply(lambda p : 'f' if p == 'm' else 'm')
#    #salary['sex'] = np.where(salary['sex'] == 'f', 'm', 'f')
#    return salar

def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
    if not pd.api.types.is_categorical_dtype(salary["sex"]):
        salary["sex"] = salary["sex"].astype("category")
    salary["sex"] = salary["sex"].cat.rename_categories({"m": "f", "f": "m"})
    return salary
print(swap_salary(salary_df))