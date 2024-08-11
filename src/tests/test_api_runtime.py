from fastapi.testclient import TestClient
import os
import json

from ..app.main import app, API_VERSION
from ..app.utils import load_env

# setup
load_env()

client = TestClient(app)

# utilities

def test_health():
    response = client.get(f'/api/{API_VERSION}/health_check')
    assert response.status_code == 200
    assert response.json() == {'message': 'The API is healthy!'}

# default

def test_predict():
    data = {
        "sepal_length": 0,
        "sepal_width": 0,
        "petal_length": 0,
        "petal_width": 0
        }
    response = client.post(f'/api/{API_VERSION}/predict', content=json.dumps(data))
    assert response.status_code == 200
    assert response.json()['errors'] is None

# mock endpoints

def test_fetch_input():
    data = {
        "sepal_length": 1.1,
        "sepal_width": 1.1,
        "petal_length": 1.1,
        "petal_width": 1.1
        } 
    response = client.get(f'/api/{API_VERSION}/example_input')
    assert response.status_code == 200
    assert response.json() == data

def test_post_input():
    data = {
        "sepal_length": 0,
        "sepal_width": 0,
        "petal_length": 0,
        "petal_width": 0
        }
    response = client.post(f'/api/{API_VERSION}/example_input', content=json.dumps(data))
    assert response.status_code == 200

def test_get_output():
    data = {
        'errors': None,
        'prediction': 1.0
    }
    response = client.get(f'/api/{API_VERSION}/example_output')
    assert response.status_code == 200
    assert response.json() == data