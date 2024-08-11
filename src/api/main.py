import logging
logging.basicConfig(level=logging.INFO)
# logging.info("__package__, __name__ ==", __package__, __name__)

import os
import json
from pathlib import Path
from fastapi import FastAPI, HTTPException
from typing import Any
import pandas as pd
import xgboost as xgb

# TODO figure out how to handle docker launch and python debug more seamlessly
try:
    from .schemas import PredictResponse, InputData, HealthResponse, InputContractData, OutputContractData
    from .utils import load_env
except Exception as e:
    from schemas import PredictResponse, InputData, HealthResponse, InputContractData, OutputContractData
    from utils import load_env

# setup
load_env()
MODEL_FILE = os.getenv('MODEL_FILE')
API_VERSION = "v1"

# Instantiate and intialize API
app = FastAPI()

model = xgb.Booster()
logging.info(f'loading model from MODEL_FILE={MODEL_FILE}')
model.load_model(MODEL_FILE)


# endpoints

@app.post(f"/api/{API_VERSION}/predict", response_model=PredictResponse)
def predict(input_data: InputData) -> Any:
    """Make predictions with the model"""
    try:
        data = pd.DataFrame.from_records([input_data.model_dump()])
        inputs = xgb.DMatrix(data=data)
        prediction = float(model.predict(inputs)[0])

        logging.info(f'Made prediction={prediction} for input={input_data.model_dump()}')

        return {
            "errors": None,
            "prediction": prediction
            }
    except Exception as e:
        raise HTTPException(status_code=500, detail={'error': str(e), 'prediction': None})

# mock api structures

@app.get(f'/api/{API_VERSION}/example_input', response_model=InputContractData, tags=['mock endpoints'])
def fetch_input_example() -> dict:
    return InputContractData().model_dump()

@app.post(f'/api/{API_VERSION}/example_input', response_model=OutputContractData, tags=['mock endpoints'])
def validate_input_example(input_data: InputContractData) -> dict:
    return OutputContractData().model_dump()

@app.get(f'/api/{API_VERSION}/example_output', response_model=OutputContractData, tags=['mock endpoints'])
def fetch_output_example() -> dict:
    return OutputContractData().model_dump()

# utilities

@app.get(f'/api/{API_VERSION}/health_check', tags=['utilities'], response_model=HealthResponse, status_code=200)
def health_check() -> dict:
    health = HealthResponse(message='The API is healthy!')
    return health.model_dump()




if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)