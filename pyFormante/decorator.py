from .util import all_forms, query_methods, query_method
from .exceptions import FormExistsException


def has_formante_form(form_name):
    def wrap(cls):
        if form_name not in all_forms:
            all_forms[form_name] = cls
        else:
            raise FormExistsException("Form name {} is already in use.".format(form_name))
        return cls
    return wrap


def is_query_method(wrapped):
    query_methods.append(wrapped)
    return wrapped


def form_generator(wrapped):
    def wrap(cls, object_id=None, form_data=None):
        form = wrapped()
        if object_id is not None:
            query = query_method()
            obj = query(cls, object_id)
            if obj is not None:
                for field_name in form.__dict__.keys():
                    attribute_name = form.__dict__[field_name].attr
                    value = obj.__dict__[attribute_name]
                    form.__dict__[field_name].data = value
        elif form_data is not None:
            for field_name in form_data.keys():
                if field_name in form.__dict__.keys():
                    form.__dict__[field_name].data = form_data[field_name]
        return form
    return classmethod(wrap)