from .validator import Validator
from ..util import register_as_validator


class DataRequired(Validator):
    __validator_name__ = 'data_required'

    def validate(self, data, request=None, session=None):
        if isinstance(data, str) or isinstance(data, unicode):
            d = data.strip()
        else:
            d = data
        return d not in ['', None]


register_as_validator(DataRequired)