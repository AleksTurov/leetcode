import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores.sort_values(by=['score'], ascending=False, inplace=True)
    scores['max_rank'] = scores['score'].rank(method='max', ascending=False)
    return scores

data = {
            'id': [1, 2, 3, 4, 5, 6],
            'score': [3.50, 3.65, 4.00, 3.85, 4.00, 3.65]
        }
scores_df = pd.DataFrame(data)
ranked_scores = order_scores(scores_df)
print(ranked_scores)

    