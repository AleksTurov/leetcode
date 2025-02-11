import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather['recordDate'] = pd.to_datetime(weather['recordDate'])
    weather_shifted = weather.copy()
    weather_shifted['recordDate'] = weather_shifted['recordDate'] + pd.to_timedelta(1, unit='D')
    merged_df = pd.merge(weather, weather_shifted, on='recordDate', suffixes=('_today', '_yesterday'))
    result = merged_df[merged_df['temperature_today'] > merged_df['temperature_yesterday']][['id_today']].rename(columns={'id_today': 'Id'})

    return result


data = {
    'id': [1, 2],
    'recordDate': ['2015-01-01', '2015-01-02'],
    'temperature': [3, 5]
}
weather_df = pd.DataFrame(data)
result = rising_temperature(weather_df)
print(result)
