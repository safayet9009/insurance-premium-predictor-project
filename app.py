from fastapi import FastAPI, HTTPException

from schema.user_input import UserInput
from schema.prediction_response import PredictionResponse

from model.predict import (
    predict_output,
    model,
    MODEL_VERSION
)


app = FastAPI(
    title="Insurance Premium Prediction API",
    description="Machine Learning API for predicting insurance premium categories",
    version=MODEL_VERSION
)


# -----------------------------
# Home
# -----------------------------

@app.get("/")
def home():

    return {
        "message": "Insurance Premium Prediction API",
        "version": MODEL_VERSION
    }


# -----------------------------
# Health Check
# -----------------------------

@app.get("/health")
def health_check():

    return {
        "status": "OK",
        "version": MODEL_VERSION,
        "model_loaded": model is not None
    }


# -----------------------------
# Prediction
# -----------------------------

@app.post(
    "/predict",
    response_model=PredictionResponse
)
def predict_premium(data: UserInput):

    user_input = {
        "bmi": data.bmi,
        "age_group": data.age_group,
        "lifestyle_risk": data.lifestyle_risk,
        "city_tier": data.city_tier,
        "income_lpa": data.income_lpa,
        "occupation": data.occupation
    }

    try:

        prediction = predict_output(user_input)

        return prediction

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )