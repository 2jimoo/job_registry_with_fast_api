class NotFoundEntityError(BaseException):
    def __init__(self, cls: type, field_name: str, field_value: object):
        self.msg = f'{cls}({field_name}:{field_value}) is not found.'

    def __str__(self):
        return self.msg


class DuplicatedEntityError(BaseException):
    def __init__(self, cls: type, field_name: str, field_value: object):
        self.msg = f'{cls}({field_name}:{field_value}) already exists.'

    def __str__(self):
        return self.msg


class InvalidArgumentError(BaseException):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class UnexpectedRequestFailError(BaseException):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


'''
파이썬3 에서는 BaseException 내장 클래스를 상속받는 클래스만이 예외 클래스로 인식되기 때문이다.
따라서 만약 예외 클래스를 인자로 받아야 하는 자리에 예외 클래스로 인식되지 않는 (BaseExeption을 상속받지 않는) 클래스를 적어놓는 경우 위와 같은 에러 메시지를 보게 된다.
'''
