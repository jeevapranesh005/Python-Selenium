class Error(Exception):
    """Base class for other exception"""
    pass
class ValueTooSmallError(Error):
    """Raised when the input value is too small"""
    pass
class ValueTooLargeError(Error):
    """Raised when the value is too large"""
    pass

number =10
while True:
    try:
        i_number=int(input("ENTER THE NUMBER"))
        if(i_number<number):
            raise ValueTooSmallError
    except ValueTooSmallError:
        print("small")

print("finish")