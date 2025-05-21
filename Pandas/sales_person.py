import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    company.rename(columns={'name': 'name_company'}, inplace=True)
    orders = orders.merge(company, on='com_id', how='inner')
    sales_person = sales_person.merge(orders, on='sales_id', how='left')
    person_red = sales_person[sales_person['name_company'] == 'RED']['name'].unique()
    result = sales_person[~sales_person['name'].isin(person_red)][['name']].drop_duplicates().reset_index(drop=True)

    return result
