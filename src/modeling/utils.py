import json
from pathlib import Path

def add_info_to_model_file(model_file, **kwargs):
    model = json.loads(Path(model_file).read_text())

    for k, v in kwargs.items():
        model['learner'][k] = v

    Path(model_file).write_text(json.dumps(model))