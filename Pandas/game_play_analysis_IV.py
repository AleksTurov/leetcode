import pandas as pd


activity = pd.DataFrame({'player_id' : [1, 1, 2, 3, 3],
                         'device_id' : [2, 2, 3, 1, 4],
                         'event_date' : ['2016-03-01', '2016-03-02', '2017-06-25', '2016-03-02', '2016-07-03'],
                         'games_played' : [5, 6, 1, 0, 5]
                        })


def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity['event_date'] = pd.to_datetime(activity['event_date'])
    activity['first_event_date'] = activity.groupby('player_id')['event_date'].transform('min')
    activity['delta_days'] = (activity['event_date'] - activity['first_event_date']).dt.days
    count_last_day = len(activity[activity['delta_days'] == 1])
    count_player = len(activity['player_id'].unique())  
    fraction = count_last_day / count_player


    return pd.DataFrame({'fraction': [round(fraction, 2)]})


print(gameplay_analysis(activity))
    