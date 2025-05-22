import pandas as pd
import numpy as np

# Create the DataFrame
data = {
    'id': [1, 2, 3, 4, 5],
    'p_id': [np.nan, 1, 1, 2, 2]
}
tree = pd.DataFrame(data)
def tree_node(tree: pd.DataFrame) -> pd.DataFrame:
    # Leaf: id не встречается в p_id
    is_leaf = ~tree['id'].isin(tree['p_id'])
    # Root: p_id is null
    is_root = tree['p_id'].isnull()
    # Inner: не root и не leaf
    types = np.where(is_root, 'Root', np.where(is_leaf, 'Leaf', 'Inner'))
    return pd.DataFrame({'id': tree['id'], 'type': types})

print(tree_node(tree))
