import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    """
    Count the number of unique subjects each teacher teaches.
    :param teacher: pd.DataFrame with columns teacher_id and subject_id
    :return: pd.DataFrame with columns teacher_id and cnt
    """
    teacher = teacher.groupby('teacher_id')['subject_id'].nunique().reset_index()
    teacher.rename(columns={'subject_id': 'cnt'}, inplace=True)
    return teacher

teacher = pd.DataFrame({
    'teacher_id': [1, 1, 2, 2, 2],
    'subject_id': [1, 2, 1, 3, 4],
    'dept_id ': [1, 1, 2, 2, 2]
})

print(count_unique_subjects(teacher))
