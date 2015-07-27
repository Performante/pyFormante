from .field import Field
from .exceptions import NotAFieldException
import json


class Form(object):
    def __init__(self, **kwargs):
        for key, value in kwargs.iteritems():
            if isinstance(value, Field):
                setattr(value, '__form__', self)
                setattr(value, '__field_name__', key)
                setattr(self, key, value)
            else:
                raise NotAFieldException()

    @property
    def _fields(self):
        fields = []
        for key in self.__dict__.keys():
            field = self.__dict__[key]
            if isinstance(field, Field):
                fields.append(field)
        return fields

    def validate(self, field_name=None, request=None, session=None):
        errors = 0
        for field in self._fields:
            if field_name is not None:
                if field.__field_name__ != field_name:
                    continue
            if not field.validate(request=request, session=session):
                errors += 1
        return False if errors > 0 else True

    def to_dict(self):
        return_dict = {}
        for field in self._fields:
            return_dict[field.__field_name__] = field.to_dict()
        return return_dict

    def to_jsons(self):
        return json.dumps(self.to_dict())