import util
from .exceptions import FormExistsException


def has_formante_form(form_name):
    def wrap(cls):
        if form_name not in util.all_forms:
            util.all_forms[form_name] = cls
            setattr(cls, '__form_name__', form_name)
        else:
            raise FormExistsException("Form name {} is already in use.".format(form_name))
        return cls
    return wrap


def is_query_method(wrapped):
    util.query = wrapped
    return wrapped


def is_query_all_method(wrapped):
    util.query_all = wrapped
    return wrapped


def form_generator(wrapped):
    def wrap(cls, object_id=None, form_data=None, request=None, session=None):
        form = wrapped(cls)
        if object_id is not None:
            obj = util.query(cls, object_id, request=request, session=session)
            if obj is not None:
                for field_name in form.__dict__.keys():
                    attribute_name = form.__dict__[field_name].attr
                    value = obj.__dict__[attribute_name]
                    form.__dict__[field_name].data = value
        elif form_data is not None:
            for field_name in form_data.keys():
                if field_name in form.__dict__.keys():
                    form.__dict__[field_name].data = form_data[field_name]
        setattr(form, '__form_name__', cls.__form_name__)
        setattr(form, '__form_attached_to__', cls)
        return form
    return classmethod(wrap)