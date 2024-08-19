import pickle
from flask import Flask, render_template, request

import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler

from src.pipeline.prediction_pipeline import CustomData, PredictPipeline

application = Flask(__name__)

app=application

# Route for Home Page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        try:
            data = CustomData(
                gender=request.form.get('gender'),
                race_ethnicity=request.form.get('race_ethnicity'),
                parental_education=request.form.get('parental_education'),
                lunch=request.form.get('lunch'),
                test_preparation_course=request.form.get('test_preparation_course'),
                writing_score=float(request.form.get('writing_score')),
                reading_score=float(request.form.get('reading_score'))
            )

            pred_df = data.get_data_as_dataframe()
            print(pred_df)

            predict_pipeline = PredictPipeline()
            results = predict_pipeline.predict(pred_df)

            return render_template('home.html', results=results[0])
        except Exception as e:
            print(f"Error occurred: {e}")
            return render_template('home.html', results="Error occurred during prediction.")

if __name__=='__main__':
    app.run(host="0.0.0.0")