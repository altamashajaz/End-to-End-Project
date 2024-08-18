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