import json
from .exceptions import ValidatorExistsException

all_forms = {}
all_validators = {}
query_methods = []


def get_form(form_name, object_id=None, form_data=None, to_dict=False, request=None, session=None):
    if form_name in all_forms:
        cls = all_forms[form_name]
        form_method = getattr(cls, "__form__", None)
        if callable(form_method):
            form = form_method(object_id=object_id, form_data=form_data, request=request, session=session)
            return form.to_dict() if (to_dict is not None and to_dict) else form
    else:
        return {} if (to_dict is not None and to_dict) else None


def get_validator_from_data(data):
    if '__validator_name__' in data:
        validator_name = data['__validator_name__']
        validator_data = dict((k, data[k]) for k in data if k != '__validator_name__')
        if validator_name in all_validators:
            cls = all_validators[validator_name]
            return cls(**validator_data)

    return None


def register_as_validator(cls):
    validator_name = cls.__validator_name__
    if validator_name not in all_validators:
        all_validators[validator_name] = cls
    else:
        raise ValidatorExistsException("Validator name {} is already in use.".format(validator_name))


def validate_form(form_name, form_data, request=None, session=None):
    if form_name in all_forms:
        cls = all_forms[form_name]
        form_method = getattr(cls, "__form__", None)
        if callable(form_method):
            return form_method(form_data=form_data).validate()


def validate_field():
    pass


def query_method():
    if len(query_methods) > 0:
        return query_methods[-1]
    else:
        raise Exception("Formante: Query method is not defined")