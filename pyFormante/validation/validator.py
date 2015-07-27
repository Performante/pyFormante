import json
from ..exceptions import ValidatorExistsException, ValidatorIncorrectException


class Validator(object):
    def __init__(self):
        pass

    __validator_name__ = None

    def validate(self, data, request=None, session=None):
        raise ValidatorIncorrectException('Validation is not implemented.')

    def to_dict(self):
        return_dict = {}

        if self.__validator_name__ is not None:
            return_dict['__validator_name__'] = self.__validator_name__
        else:
            raise ValidatorIncorrectException('Validator name is not set.')

        for key in self.__dict__.keys():
            if key not in ['__field__']:
                return_dict[key] = self.__dict__[key]
        return return_dict

    def to_jsons(self):
        return json.dumps(self.to_dict())