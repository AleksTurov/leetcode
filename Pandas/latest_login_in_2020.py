import pandas as pd

# Sample data
data = {
    'user_id': [6, 6, 6, 8, 8, 2, 2, 14, 14],
    'time_stamp': [
        '2020-06-30 15:06:07', '2021-04-21 14:06:06', '2019-03-07 00:18:15',
        '2020-02-01 05:10:53', '2020-12-30 00:46:50', '2020-01-16 02:49:50',
        '2019-08-25 07:59:08', '2019-07-14 09:00:00', '2021-01-06 11:59:59'
    ]
}

# Create DataFrame
logins = pd.DataFrame(data)
logins['time_stamp'] = pd.to_datetime(logins['time_stamp'])

print(logins)
import pandas as pd

def latest_login(logins: pd.DataFrame) -> pd.DataFrame:
    logins = logins[((logins['time_stamp'] < '2021-01-01') & (logins['time_stamp'] >= '2020-01-01'))]
    logins = logins.sort_values(by='time_stamp', ascending=False)
    logins.drop_duplicates(subset='user_id', keep='first', inplace=True)
    logins.rename(columns={'time_stamp': 'last_stamp'}, inplace=True)
    return logins
    
logins = pd.DataFrame(latest_login(logins))
print(logins)