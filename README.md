# Machine Learning API

This repo is a template for ML training and serving. 

# Quick Deploy

The repo contains a demo which can immediately be deployed.

- `bash run.sh`
- Api will be available at `localhost:80`

# Developer Setup

1. Create python virtual env
    - `python3 -m venv .venv`
2. Activate virtual env
    - linux: `source .venv/bin/activate`
    - windows: `.venv/Scripts/activate.bat`
3. Install requirements
    - `pip install -r requirements-dev.txt`

# Use

0. Training/serving is controlled by a `MODEL_FILE` paramter in `.env`
    - this is already set to a default value that references examples included in this template
1. Create a new ML model
    - A template is available at `src/modeling/train.ipynb` for creating an XGBoost model
    - The model save outputs an additional json artifact leveraged by the API
2. Develop the API with the debugger
    - VSCode Users:
        - Setup interpreter: `Ctrl+Shift+p` and search for 'select interpreter' and choose your venv
        - Debug mode already configured for you as `Python: API`
    - Other IDEs:
        - Run the `src/app/api/main.py` file in debug mode
    - Swagger page available at `localhost:8000` for testing
3. Launch API "service" containerized with hot-reload enabled
    - VSCode Users: 
        - `Ctrl+Shift+B`
    - Other IDEs: 
        - `docker compose up --build --remove-orphans`
    - Swagger page available at `localhost:80` for testing

# Testing

- Pytest autoparsing is used to locate tests
- Run test suite with a coverage report with `coverage run --data-file=artifacts/.coverage -m pytest`
- `coverage report --data-file=artifacts/.coverage`