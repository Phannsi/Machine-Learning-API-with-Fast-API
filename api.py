from fastapi import FastAPI
import joblib
from pydantic import BaseModel
import pandas as pd


app = FastAPI()

class PatientResults(BaseModel):
    PRG: float
    PL: float
    PR: float
    SK: float
    TS: float
    M11: float
    BD2: float
    Age: int


@app.get('/')
def status_check():
    return{'Status':'API is online'}

logistic_regression_pipeline = joblib.load('./models and encoder/Logistic_regression_pipeline.joblib')
random_forest_pipeline = joblib.load('./models and encoder/Random_forest_pipeline.joblib')
encoder = joblib.load('./models and encoder/encoder.joblib')

@app.post('/Logistic_regression_prediction')
def make_prediction(data: PatientResults):
    df = pd.DataFrame([data.model_dump()])

    prediction = logistic_regression_pipeline.predict(df)

    prediction = encoder.inverse_transform([prediction])[0]

    probability = logistic_regression_pipeline.predict_proba(df)
    probability = probability[0]

    # Prepare the result dictionary
    result = {
        'Prediction': prediction,
        'Probability': {
            'Positive': round(probability[1] * 100, 2),
            'Negative': round(probability[0] * 100, 2)
        },
        'Message': 'Your Patient will develop Sepsis' if prediction == 'Positive' else 'Your Patient will not develop Sepsis'
    }

    return result
    
@app.post('/Random_forest_prediction')
def make_prediction(data: PatientResults):
    df = pd.DataFrame([data.model_dump()])

    prediction = random_forest_pipeline.predict(df)

    prediction = encoder.inverse_transform([prediction])[0]

    probability = random_forest_pipeline.predict_proba(df)
    probability = probability[0]

  # Prepare the result dictionary
    result = {
        'Prediction': prediction,
        'Probability': {
            'Positive': round(probability[1] * 100, 2),
            'Negative': round(probability[0] * 100, 2)
        },
        'Message': 'Your Patient will develop Sepsis' if prediction == 'Positive' else 'Your Patient will not develop Sepsis'
    }

    return result