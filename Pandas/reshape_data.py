import pandas as pd

# Sample data
data = {
    'city': ['Jacksonville', 'Jacksonville', 'Jacksonville', 'Jacksonville', 'Jacksonville', 
             'ElPaso', 'ElPaso', 'ElPaso', 'ElPaso', 'ElPaso'],
    'month': ['January', 'February', 'March', 'April', 'May', 
              'January', 'February', 'March', 'April', 'May'],
    'temperature': [13, 23, 38, 5, 34, 20, 6, 26, 2, 43]
}
def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    df = pd.pivot_table(weather, index='month', columns='city', values='temperature', aggfunc='mean')
    
    return df
    
# Create DataFrame
weather = pd.DataFrame(data)
print(weather)
print(pivotTable(weather))