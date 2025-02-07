import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    person = person.groupby('email').filter(lambda x: len(x) > 1)
    person.rename(columns={'email': 'Email'}, inplace=True)
    return person[['Email']].drop_duplicates()

person = pd.DataFrame({
    'id': [1, 2, 3],
    'email': ['a@b.com', 'c@d.com', 'a@b.com']
})

df = duplicate_emails(person)
print(df)
