import os
import sys

from dataclasses import dataclass

from sklearn.ensemble import AdaBoostRegressor, GradientBoostingRegressor, RandomForestRegressor
from sklearn.linear_model import LinearRegression, Ridge, Lasso

from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from xgboost import XGBRegressor
from sklearn.metrics import r2_score

from src.exception import CustomException
from src.logger import logging

from src.utilis import save_object, evaluate_model

@dataclass
class ModelTrainerConfig:
    trained_model_path = os.path.join('artifacts', "model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_arr, test_arr):
        try:
            logging.info("Spliting Train and Test Input Data")
            X_train, y_train, X_test, y_test = (train_arr[:,:-1], 
                                                train_arr[:,-1], 
                                                test_arr[:,:-1], 
                                                test_arr[:,-1])
            models = {
                'Linear Regression':LinearRegression(),
                'Ridge Regression' : Ridge(),
                'Lasso Regression': Lasso(),
                "K-Neighbors": KNeighborsRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Random Forest": RandomForestRegressor(),
                "AdaBoost": AdaBoostRegressor(),
                'GredientBoost': GradientBoostingRegressor(),
                "XGBoost": XGBRegressor(),

            }

            logging.info("Model Training and Evaluation Started")
            model_report:dict=evaluate_model(X_train=X_train, y_train=y_train,
                                              X_test=X_test, y_test=y_test, models=models)
            
            # Get the best model score from dict
            best_model_score = max(sorted(model_report.values()))

            # Get the model name from the dict
            best_model_name =  list(model_report.keys())[list(model_report.values()).index(best_model_score)]

            best_model = models[best_model_name]

            if best_model_score<0.6:
                raise CustomException("No best Model Found")
            
            logging.info(f"Best model is: {best_model_name} with r2_score: {best_model_score}")

            save_object(filepath=self.model_trainer_config.trained_model_path, obj=best_model)

            y_preds = best_model.predict(X_test)

            r2_scr = r2_score(y_test, y_preds)

            return r2_scr

        except Exception as e:
            raise CustomException(e, sys)
