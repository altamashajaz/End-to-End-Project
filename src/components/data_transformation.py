import sys
import os
from dataclasses import dataclass

import numpy as np
import pandas as pd

from src.logger import logging
from src.exception import CustomException
from src.utilis import save_object

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

@dataclass
class DataTransformationConfig:
    preprocessor_obj_filepath = os.path.join('artifacts', 'preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transferconfig = DataTransformationConfig()
    
    def get_data_transformer_obj(self):
        try:
            numeric_column = ['writing score', 'reading score']
            categorical_column = [
                'gender',
                'lunch',
                'race/ethnicity',
                'parental level of education',
                'test preparation course'
            ]

            num_pipeline = Pipeline(
                steps=[
                    ("Imputer", SimpleImputer(strategy='median')),
                    ('Scaler', StandardScaler())
                ])
            
            cat_pipeline = Pipeline(
                steps=[
                    ('Imputing', SimpleImputer(strategy='most_frequent')),
                     ('OneHotEncode', OneHotEncoder(drop='first'))
                ])
            

            preprocesser = ColumnTransformer(
                [
                    ('num_pipeline', num_pipeline, numeric_column),
                    ('cat_pipeline', cat_pipeline, categorical_column)
                ])
            logging.info('Standarization and OneHotEncoding of Numerical and Categorical Coulmn Done')

            return preprocesser
        except Exception as e:
            raise CustomException(e, sys)
    
    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info('Imported Train and Test Data in form of DataFrame')

            logging.info("Obtaining Preprocessing Object")

            preprocessing_obj = self.get_data_transformer_obj()

            target_column_name = 'math score'

            numeric_column = ['writing score', 'reading score']

            input_feature_train_df = train_df.drop(target_column_name, axis=1)

            input_feature_test_df = test_df.drop(target_column_name, axis=1)

            logging.info("Appling Preprocessor Object on Training and Test Dataframe")

            input_feature_train_array = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_array = preprocessing_obj.transform(input_feature_test_df)

            train_arr = np.c_[input_feature_train_array, np.array(train_df[target_column_name])]
            test_arr = np.c_[input_feature_test_array, np.array(test_df[target_column_name])]

            logging.info("Saving Preprocessing Objects")

            save_object(
                filepath = self.data_transferconfig.preprocessor_obj_filepath,
                obj = preprocessing_obj
            )

            return (
                train_arr,
                test_arr,
                self.data_transferconfig.preprocessor_obj_filepath
            )
        except Exception as e:
            raise CustomException(e, sys)


