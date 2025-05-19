import pandas as pd
data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8],
    'visit_date': [
        '2017-01-01', '2017-01-02', '2017-01-03', '2017-01-04',
        '2017-01-05', '2017-01-06', '2017-01-07', '2017-01-09'
    ],
    'people': [10, 109, 150, 99, 145, 1455, 199, 188]
}

df = pd.DataFrame(data)

def human_traffic(stadium: pd.DataFrame) -> pd.DataFrame:
    stadium = stadium.sort_values('id').reset_index(drop=True)
    mask = stadium['people'] >= 100

    # Проверяем для каждой строки, входит ли она в любую тройку подряд с people >= 100
    cond1 = mask & mask.shift(-1, fill_value=False) & mask.shift(-2, fill_value=False)
    cond2 = mask & mask.shift(1, fill_value=False) & mask.shift(-1, fill_value=False)
    cond3 = mask & mask.shift(1, fill_value=False) & mask.shift(2, fill_value=False)

    final_mask = cond1 | cond2 | cond3

    result = stadium[final_mask].copy()
    result = result[['id', 'visit_date', 'people']].sort_values('visit_date').reset_index(drop=True)
    return result

print(human_traffic(df))
    