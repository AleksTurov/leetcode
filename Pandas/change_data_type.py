import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students['grade'] = students['grade'].astype(int)
    return students
    
# Test
students = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'grade': ['90', '80', '70']
})
print(changeDatatype(students))
