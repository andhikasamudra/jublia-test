validate_schema = {
    "type": "object",
    "properties": {
        "event_id": {"type": "integer"},
        "subject": {"type": "string"},
        "content": {"type": "string"},
        "sent_timestamp": {"type": "string", "format": "custom-date-time"},
    },
    "required": ["subject", "content", "event_id", "sent_timestamp"],
    "additionalProperties": False,
    "definitions": {
        "custom-date-time": {
            "type": "string",
            "pattern": "^[0-9]{1,2} [A-Za-z]{3} [0-9]{4} [0-9]{2}:[0-9]{2}$",
        }
    },
}
