import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

from features.feature_engineering import feature_engineering

import mlflow

TEST_SIZE = 0.2
RANDOM_STATE = 42

def load_data(path):

    data = pd.read_csv(path)

    mlflow.log_artifact(data) # Логируем данные как артефакт, датасет оказался обработанным.

    X = data.drop(['GradeClass', 'StudentID'], axis=1)
    y = data['GradeClass']

    X = feature_engineering(X)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE)

    return X_train, X_test, y_train, y_test
    
