# Student-Performance-Predictor

## Overview

This project is an end-to-end machine learning solution designed to predict student performance using key features like parents' education, lunch type, race/ethnicity, and reading and writing scores. The repository includes exploratory data analysis (EDA), model training, and a Flask-based web application for real-time predictions. The project is built using modular programming for clean, maintainable code and deployed using AWS Elastic Beanstalk and CodePipeline.

## Project Structure

- **`notebook/`**: Jupyter notebooks for EDA and model training.
- **`src/`**: Source code for data preprocessing, model building, and evaluation.
- **`templates/`**: HTML templates for the web application.
- **`app.py`**: Flask application script for deployment.
- **`requirements.txt`**: Dependencies list.
- **`setup.py`**: Script for setting up the package.

## Tools Used

- **Python**: Core programming language for the project.
- **Pandas & NumPy**: Data manipulation and analysis.
- **Matplotlib & Seaborn**: Data visualization.
- **Scikit-learn**: Machine learning model building and evaluation.
- **Flask**: Web framework for deploying the model.
- **AWS Elastic Beanstalk & CodePipeline:** Deployment of the web application
- **Jupyter Notebook**: Interactive environment for EDA and model training.

## Key Features

1. **Exploratory Data Analysis**:
   - Comprehensive data exploration with visualizations.
   - Key insights into factors affecting student performance.

2. **Model Training**:
   - Custom-built modules for data preprocessing and model evaluation.
   - Implementation of machine learning algorithms to predict outcomes.

3. **Deployment:**
   - Flask-based web application allowing real-time predictions.
   - Deployed using AWS Elastic Beanstalk and CodePipeline.

## Installation

1. Clone the repository:
```bash
   git clone https://github.com/altamashajaz/Student-Performance-Predictor.git
```

2. Install dependencies:
```bash
cd Student-Performance-Predictor
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

## **Usage**
1. Explore the dataset using the EDA notebook to identify key factors.
2. Train the model using the training notebook and customize it as needed.
3. Deploy the model using app.py and interact with the web interface to predict student performance.


## 📊 Features
- Data Preprocessing: Handles missing data, feature engineering, and normalization.
- Model Training & Evaluation: Implements multiple ML models with cross-validation.
- Web Interface: Flask app for user input and model predictions.

## Live Application

You can access the live application [here](http://studentperformance-env.eba-hgt29p3d.ap-south-1.elasticbeanstalk.com).

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss any changes.

## Contact

For any queries or issues, please contact [Altamash Ajaz](https://github.com/altamashajaz).