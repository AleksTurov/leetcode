import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee = employee.drop_duplicates(subset=['salary']).sort_values(by='salary', ascending=False)
    if N <= 0 or N > len(employee):
        nth_salary = pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    else:
        nth_salary = employee[['salary']].iloc[N-1:N]
        nth_salary.columns = [f'getNthHighestSalary({N})']
    return nth_salary

# Test
employee = pd.DataFrame({
    'name': ['John', 'Emma', 'Alex', 'Tom', 'James'],
    'salary': [10000, 20000, 15000, 25000, 30000]
})
print(nth_highest_salary(employee, 3))