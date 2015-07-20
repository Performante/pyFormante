from .field import Field
from .exceptions import NotAFieldException
import json


class Form(object):
    def __init__(self, **kwargs):
        for key, value in kwargs.iteritems():
            if isinstance(value, Field):
                setattr(self, key, value)
            else:
                raise NotAFieldException()

    def validate(self):
        errors = 0
        for key in self.__dict__.keys():
            if not self.__dict__[key].validate():
                errors += 1
        return False if errors > 0 else True

    def validate_field(self, field_name):
        pass

    def to_dict(self):
        return_dict = {}
        for key in self.__dict__.keys():
            return_dict[key] = self.__dict__[key].to_dict()
        return return_dict

    def to_jsons(self):
        return json.dumps(self.to_dict())