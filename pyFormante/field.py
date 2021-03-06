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


class Field(object):
    def __init__(self, attr, type=InputType.text, validation=None):
        self.attr = attr
        self.data = None
        self.type = type
        self.validation = validation if validation is not None else []
        for validator in self.validation:
            setattr(validator, '__field__', self)

    def validate(self, request=None, session=None):
        errors = 0
        for validator in self.validation:
            if not validator.validate(self.data, request=request, session=session):
                errors += 1
        return False if errors > 0 else True

    def to_dict(self):
        dict = {
            'type': self.type.value,
            'data': self.data,
        }

        validation = []
        for validator in self.validation:
            validation.append(validator.to_dict())
        dict['validation'] = validation

        return dict

    def to_jsons(self):
        return json.dumps(self.to_dict())