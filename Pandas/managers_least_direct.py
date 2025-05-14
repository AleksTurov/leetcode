import pandas as pd

# The function takes a DataFrame as input and returns a DataFrame
# with the names of managers who have at least 5 direct reports.

# Create a DataFrame for the Employee table
data = {
    'id': [101, 102, 103, 104, 105, 106],
    'name': ['John', 'Dan', 'James', 'Amy', 'Anne', 'Ron'],
    'department': ['A', 'A', 'A', 'A', 'A', 'B'],
    'managerId': [None, 101, 101, 101, 101, 101]
}
employee = pd.DataFrame(data)

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    employee_gr = employee.groupby('managerId')['id'].count().reset_index()
    employee_gr = employee_gr.query('id >= 5')
    employee = employee.merge(employee_gr, how='inner', left_on='id', right_on = 'managerId')
    return employee[['name']]

# Call the function and print the result
result = find_managers(employee)
print(result)