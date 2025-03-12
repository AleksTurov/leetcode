import pandas as pd

def capital_gainloss(stocks: pd.DataFrame) -> pd.DataFrame:
    stocks = pd.pivot_table(stocks, values='price', index=['stock_name'], columns=['operation'], aggfunc='sum').reset_index()
    stocks['capital_gain_loss'] = stocks['Sell'] - stocks['Buy']
    return stocks[['stock_name', 'capital_gain_loss']] 

# Create a DataFrame
data = {
    'stock_name': ['Leetcode', 'Corona Masks', 'Leetcode', 'Handbags', 'Corona Masks', 
                   'Corona Masks', 'Corona Masks', 'Corona Masks', 'Handbags', 'Corona Masks'],
    'operation': ['Buy', 'Buy', 'Sell', 'Buy', 'Sell', 'Buy', 'Sell', 'Buy', 'Sell', 'Sell'],
    'operation_day': [1, 2, 5, 17, 3, 4, 5, 6, 29, 10],
    'price': [1000, 10, 9000, 30000, 1010, 1000, 500, 1000, 7000, 10000]
}

df = pd.DataFrame(data)

print(capital_gainloss(df))