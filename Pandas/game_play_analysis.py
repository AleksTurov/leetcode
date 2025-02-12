import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity = activity.sort_values(by='event_date').groupby('player_id', as_index=False).first()
    activity = activity[['player_id', 'event_date']].rename(columns={'event_date': 'first_login'})
    return activity

activity = pd.DataFrame({
    'player_id': [1, 1, 2, 3, 3],
    'device_id': [2, 2, 3, 1, 4],
    'event_date': ['2016-03-01', '2016-05-02', '2017-06-25', '2016-03-02', '2018-07-03'],
    'games_played': [5, 6, 1, 0, 5]
})

df = game_analysis(activity)
print(df)
