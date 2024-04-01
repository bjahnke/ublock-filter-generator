# filter_validator.py
import json
from jsonschema import validate, ValidationError

def validate_filters(filter_data):
    try:
        validate(instance=filter_data, schema=filter_schema)
    except ValidationError as e:
        raise ValueError(f"Invalid filter data: {e.message}")

filter_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "source": {"type": "string"},
            "selectors": {
                "type": "object",
                "properties": {
                    "company": {"type": "string"},
                    "title": {"type": "string"}
                },
                "required": ["company", "title"]
            },
            "filter": {"type": "string"}
        },
        "required": ["source", "selectors", "filter"]
    }
}