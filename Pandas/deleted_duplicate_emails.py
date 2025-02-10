import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values(by=['id'], ascending=True, inplace=True)
    person.drop_duplicates(subset=['email'], inplace=True, keep='first')
    return person

    

person = pd.DataFrame({
    'id': [1, 2, 3],
    'email': ['john@example.com', 'bob@example.com', 'john@example.com']
})

df = delete_duplicate_emails(person)
print(df)
