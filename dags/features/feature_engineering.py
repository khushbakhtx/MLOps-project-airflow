import pandas as pd

def feature_engineering(df):

    df['Academic_Engagement'] = (df['StudyTimeWeekly'] +  df['Tutoring'] +  df['ParentalSupport'] +  df['Extracurricular'])
    df['Parental_Involvement'] = (df['ParentalEducation'] +  df['ParentalSupport'])
    df['Absenteeism Impact'] = df['Absences'] / df['StudyTimeWeekly'].replace(0, pd.NA)
    df['Activity Diversity'] = (df[['Sports', 'Music', 'Volunteering']].sum(axis=1)) / (df[['Sports', 'Music', 'Volunteering']].count(axis=1))
    
    return df
