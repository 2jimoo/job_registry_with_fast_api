class NotFoundEntityError(Exception):
    def __init__(self, cls: type, field_name: str, field_value: object):
        self.msg = f'{cls}({field_name}:{field_value}) is not found.'

    def __str__(self):
        return self.msg


class DuplicatedEntityError(Exception):
    def __init__(self, cls: type, field_name: str, field_value: object):
        self.msg = f'{cls}({field_name}:{field_value}) already exists.'

    def __str__(self):
        return self.msg


class InvalidArgumentError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class UnexpectedRequestFailError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg
