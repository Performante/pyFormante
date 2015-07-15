from enum import Enum
import json


class InputType(Enum):
    boolean = 'checkbox'
    date = 'date'
    datetime = 'datetime'
    number = 'number'
    password = 'password'
    text = 'text'
    time = 'time'


class Field:
    def __init__(self, attr, type=InputType.text, validation=None):
        self.attr = attr
        self.data = None
        self.type = type
        self.validation = validation if validation is not None else []

    def validate(self):
        errors = 0
        for validator in self.validation:
            if not validator.validate(self.data):
                errors += 1
        return False if errors > 0 else True

    def to_dict(self):
        dict = {
            'type': self.type.value,
            'data': self.data,
        }

        validation = []
        for validator in self.validation:
            validation.append(validator.to_string())
        dict['validation'] = validation

        return dict

    def to_jsons(self):
        return json.dumps(self.to_dict())