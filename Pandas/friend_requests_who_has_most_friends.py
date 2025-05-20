import pandas as pd

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    # Stack both requester_id and accepter_id to represent all connections
    all_friends = pd.concat([
        request_accepted[['requester_id']].rename(columns={'requester_id': 'id'}),
        request_accepted[['accepter_id']].rename(columns={'accepter_id': 'id'})
    ])
    
    # Count each person's total number of friends
    friends_count = all_friends['id'].value_counts().reset_index()
    friends_count.columns = ['id', 'num']

    return friends_count.iloc[:1][['id', 'num']]

    