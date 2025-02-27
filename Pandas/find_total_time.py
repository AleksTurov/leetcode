import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = employees['out_time'] - employees['in_time']
    employees.rename(columns={"event_day": "day"}, inplace=True)
    employees = employees.groupby(['day','emp_id'])['total_time'].sum().reset_index()
    return employees

# Test
employees = pd.DataFrame({
    'emp_id': [1, 1, 2, 2],
    'event_day': ['2021-01-01', '2021-01-01', '2021-01-01', '2021-01-01'],
    'in_time': ['09:00:00', '09:00:00', '09:00:00', '09:00:00'],
    'out_time': ['17:00:00', '17:00:00', '17:00:00', '17:00:00']
})
print(total_time(employees))
