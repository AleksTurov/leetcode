import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    person.set_index('personId', inplace=True)
    address.set_index('personId', inplace=True)
    merge = person[['firstName', 'lastName']].join(address[['city', 'state']], how='left')

    return merge

person = {'personId': [1, 2, 3], 'firstName': ['John', 'Sally', 'Alice'], 'lastName': ['Doe', 'Smith', 'Johnson']}
address = {'personId': [1, 2, 4], 'city': ['Chicago', 'New York', 'Los Angeles'], 'state': ['IL', 'NY', 'CA']}
person = pd.DataFrame(person)
address = pd.DataFrame(address)
person_address = combine_two_tables(person, address)
print(person_address)