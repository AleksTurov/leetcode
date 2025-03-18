import pandas as pd
from typing import List
student_data = [
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    df = pd.DataFrame(student_data, columns=['student_id', 'age'])
    return df

print(createDataframe(student_data))