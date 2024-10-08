import sys
import pandas as pd
from src.exception import CustomException
from src.logger import logging

from src.utilis import load_object

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try: 
            model_path = r'artifacts/model.pkl'
            preprocessor_path = r'artifacts/preprocessor.pkl'

            model = load_object(filepath=model_path)
            preprocessor = load_object(filepath=preprocessor_path)
            data_scaled = preprocessor.transform(features)
            prediction = model.predict(data_scaled).round(2)

            return prediction
        except Exception as e:
            raise CustomException(e, sys)


class CustomData:
    def __init__(self,
                 gender: str, 
                 race_ethnicity: str,
                 parental_education: str,
                 lunch: str,
                 test_preparation_course: str,
                 reading_score: float, 
                 writing_score: float):
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_education = parental_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race/ethnicity": [self.race_ethnicity],
                "parental level of education": [self.parental_education],
                "lunch": [self.lunch],
                "test preparation course": [self.test_preparation_course],
                "reading score": [self.reading_score],
                "writing score": [self.writing_score]
            }

            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise CustomException(e, sys)
