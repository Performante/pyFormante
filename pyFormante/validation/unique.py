from .validator import Validator
from ..util import register_as_validator


class Unique(Validator):
    __validator_name__ = 'exact_length'

    def validate(self, data, request=None, session=None):
        pass
        return False


register_as_validator(Unique)