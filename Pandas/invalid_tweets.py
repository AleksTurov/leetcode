import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    return tweets[tweets['content'].str.len() > 15][['tweet_id']]
    
# Example usage
tweets = pd.DataFrame({
    'tweet_id': [1, 2, 3],
    'content': ['hello', 'hi', 'how are you doing today? I am doing great!']
})
print(invalid_tweets(tweets))