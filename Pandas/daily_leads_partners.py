import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    daily_sales = daily_sales.groupby(['date_id', 'make_name']).nunique().reset_index()
    daily_sales.rename(columns={'lead_id': 'unique_leads', 'partner_id': 'unique_partners'}, inplace=True)
    return daily_sales

# Test
daily_sales = pd.DataFrame({
    'date_id': ['2021-01-01', '2021-01-01', '2021-01-02', '2021-01-02'],
    'make_name': ['Toyota', 'Toyota', 'Honda', 'Honda'],
    'lead_id': [1, 2, 3, 4],
    'partner_id': [5, 6, 7, 8]
})
print(daily_leads_and_partners(daily_sales))
# Output:
#                         lead_id  partner_id
# date_id    make_name
# 2021-01-01 Toyota            2           2
# 2021-01-02 Honda             2           2            

    