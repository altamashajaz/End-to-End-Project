import os
import sys
import dill

import pandas as pd
import numpy as np

from src.exception import CustomException

def save_object(filepath, obj):
    try:
        dir_path = os.path.dirname(filepath)

        os.makedirs(dir_path, exist_ok=True)

        with open(filepath, 'wb') as file:
            dill.dump(obj, file)
        
    except Exception as e:
        raise CustomException(e, sys)

from sklearn.metrics import r2_score
def evaluate_model(X_train, y_train, X_test, y_test, models:dict):

    report = {}
    try:
    # Loop through each model in the dictionary
        for i in range(len(list(models))):
            model = list(models.values())[i]
            model.fit(X_train, y_train)  # Train the model on the training data

            # Make predictions on both training and test data
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)
            
            # Evaluate performance metrics for the training data
            train_model_score = r2_score(y_train, y_train_pred)

            # Evaluate performance metrics for the test data
            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

            return report

    except Exception as e:
        raise CustomException(e, sys)

def load_object(filepath):
    try:
        with open(filepath, 'rb') as file_obj:
            return dill.load(file_obj)
    
    except Exception as e:
        raise CustomException(e, sys)