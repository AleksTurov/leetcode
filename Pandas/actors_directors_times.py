import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    actor_director = actor_director.groupby(['actor_id', 'director_id'])['timestamp'].nunique().reset_index()
    return actor_director.query('timestamp >= 3')[['actor_id', 'director_id']]
    