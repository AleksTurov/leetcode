import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    project = project.merge(employee, on='employee_id')
    project = project.groupby('project_id')['experience_years'].mean().reset_index()
    project['experience_years'] = round(project['experience_years'], 2)
    project.rename(columns={'experience_years': 'average_years'}, inplace=True)
    return project[['project_id', 'average_years']]