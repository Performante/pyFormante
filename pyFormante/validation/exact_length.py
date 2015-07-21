from .validator import Validator
from ..util import register_as_validator


class ExactLength(Validator):
    __validator_name__ = 'exact_length'

    def __init__(self, exact_length):
        super(ExactLength, self).__init__()
        self.exact_length = exact_length

    def validate(self, data):
        return len(data) >= self.exact_length


register_as_validator(ExactLength)