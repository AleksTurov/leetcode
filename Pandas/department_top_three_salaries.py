import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    employee['rank'] = employee.groupby('departmentId')['salary'].rank(method='dense', ascending=False)
    employee = employee[employee['rank'] < 4]
    employee.rename(columns={'name':'Employee', 'salary':'Salary'}, inplace=True)
    employee = employee.merge(department, left_on='departmentId', right_on='id')
    employee.rename(columns={'name':'Department'}, inplace=True)
    return employee[['Department', 'Employee', 'Salary']]
    
if __name__ == "__main__":
    # Sample data
    employee_data = {
        'id': [1, 2, 3, 4, 5, 6],
        'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
        'salary': [70000, 80000, 90000, 60000, 50000, 40000],
        'departmentId': [1, 1, 2, 2, 3, 3]
    }
    
    department_data = {
        'id': [1, 2, 3],
        'name': ['HR', 'Engineering', 'Sales']
    }
    
    employee_df = pd.DataFrame(employee_data)
    department_df = pd.DataFrame(department_data)
    
    result = top_three_salaries(employee_df, department_df)
    print(result)
# Output:
#     Department  Employee  Salary
# 0          HR      Bob   80000
# 1          HR    Alice   70000
# 2  Engineering  Charlie   90000
# 3  Engineering    David   60000
# 4        Sales      Eve   50000
# 5        Sales    Frank   40000
