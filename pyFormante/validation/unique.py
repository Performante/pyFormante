from .validator import Validator
from ..util import register_as_validator


class Unique(Validator):
    __validator_name__ = 'exact_length'

    # def __init__(self, exact_length):
    #     super(Unique, self).__init__()
    #     self.exact_length = exact_length

    def validate(self, data):
        pass
        return False


register_as_validator(Unique)