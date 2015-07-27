from .validator import Validator
from .. import util


class Unique(Validator):
    __validator_name__ = 'unique'

    def validate(self, data, request=None, session=None):
        attr = self.__field__.attr
        cls = self.__field__.__form__.__form_attached_to__
        all = util.query_all(cls, request=request, session=session)
        for obj in all:
            if obj.__dict__[attr] == data:
                return False
        return True


util.register_as_validator(Unique)