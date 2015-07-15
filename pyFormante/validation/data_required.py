class DataRequired:
    def __init__(self):
        pass

    __validator_name__ = 'data_required'

    @staticmethod
    def validate(data):
        if isinstance(data, str) or isinstance(data, unicode):
            d = data.strip()
        else:
            d = data
        return d not in ['', None]

    @staticmethod
    def to_string():
        return DataRequired.__validator_name__