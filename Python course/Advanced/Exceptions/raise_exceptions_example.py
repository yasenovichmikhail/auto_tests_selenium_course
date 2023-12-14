class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(x):
    if x < 5:
        raise ValueTooSmallError('value is too small', x)
    
try:
    test_value(1)
except ValueTooSmallError as e:
    print(e.message, e.value)
    

    