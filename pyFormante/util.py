import json

all_forms = {}
query_methods = []


def get_form_data(form_name, object_id=None, to_string=False):
    if form_name in all_forms:
        cls = all_forms[form_name]
        form_method = getattr(cls, "__form__", None)
        if callable(form_method):
            return form_method(object_id=object_id).to_jsons() if to_string else form_method(object_id=object_id).to_dict()
    else:
        return json.dumps({}) if to_string else {}


def validate_form(form_name, form_data):
    if form_name in all_forms:
        cls = all_forms[form_name]
        form_method = getattr(cls, "__form__", None)
        if callable(form_method):
            return form_method(form_data=form_data).validate()


def validate_field():
    pass


def query_method():
    return query_methods[-1] if len(query_methods) > 0 else None