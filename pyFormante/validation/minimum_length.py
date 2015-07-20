from .validator import Validator
from ..util import register_as_validator


class MinimumLength(Validator):
    __validator_name__ = 'minimum_length'

    def __init__(self, minimum_length):
        super(MinimumLength, self).__init__()
        self.minimum_length = minimum_length

    def validate(self, data):
        return len(data) >= self.minimum_length


register_as_validator(MinimumLength)