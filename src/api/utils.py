import json
from pathlib import Path
from dotenv import load_dotenv
import os
import logging

def load_env():
    try:
        load_dotenv()
    except:
        pass

numpy_to_pydantic = {
    'int64': int,
    'float64': float,
    'object': str
}

def get_input_schema():
    load_env()
    MODEL_FILE = os.getenv('MODEL_FILE')
    model = json.loads(Path(MODEL_FILE).read_text())

    names = model['learner']['feature_names']
    types = model['learner']['feature_types']
    logging.info(f'loading input schema MODEL_FILE={MODEL_FILE} names={names} types={types}')

    # define tuple as (type, default)  ... for no default
    fields = {name: (numpy_to_pydantic[typ], ...) for name, typ in zip(names, types)}

    return fields

def get_contract_schema(path):
    p = Path(path)
    payload = json.loads(p.read_text())
    fields = {k: (type(v), v) for k,v in payload.items()}
    return fields

def get_db_params():
    load_env()

    return {
    "host": os.getenv('POSTGRES_HOST'),
    "port": os.getenv('POSTGRES_PORT'),
    "user": os.getenv('POSTGRES_USER'),
    "password": os.getenv('POSTGRES_PASSWORD'),
}