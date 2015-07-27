from .validator import Validator
from ..util import register_as_validator


class MaximumLength(Validator):
    __validator_name__ = 'maximum_length'

    def __init__(self, maximum_length):
        super(MaximumLength, self).__init__()
        self.maximum_length = maximum_length

    def validate(self, data, request=None, session=None):
        return len(data) >= self.maximum_length


register_as_validator(MaximumLength)