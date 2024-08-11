from typing import Any, List, Optional
from pydantic import BaseModel, create_model

# TODO figure out how to handle docker launch and python debug more seamlessly
try:
    from .utils import get_input_schema, get_contract_schema
except:
    from utils import get_input_schema, get_contract_schema

# single data point
class PredictResponse(BaseModel):
    errors: Optional[Any]
    prediction: Optional[Any]

InputData = create_model(
    'InputData', **get_input_schema()
)

# batch endpoint
class BatchPredictResponse(BaseModel):
    errors: Optional[Any]
    predictions: List[Optional[Any]]

# api contracts
InputContractData = create_model(
    'InputContractData', **get_contract_schema('api_contracts/in/ml_prediction.json')
)

OutputContractData = create_model(
    'OutputContractData', **get_contract_schema('api_contracts/out/ml_prediction.json')
)

# util

class HealthResponse(BaseModel):
    message: str

if __name__ == '__main__':
    health = HealthResponse()
    resposne = PredictResponse()
    input = get_input_schema()
    batchresponse = BatchPredictResponse()

