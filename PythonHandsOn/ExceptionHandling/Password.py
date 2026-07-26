class InvalidUsernameException(Exception):
    pass
class InvalidPasswordException(Exception):
    pass
def vali_username(uname):
    if len(uname) < 6 or len(uname) > 30:
        raise InvalidUsernameException(
            "Username length should be between 6 and 30 characters."
        )
    if not uname[0].isalpha():
        raise InvalidUsernameException("Username must start with an alphabet.")
    for ch in uname:
        if not (ch.isalnum() or ch == "_"):
            raise InvalidUsernameException("Username can contain only letters, digits and underscore.")
def vali_password(ps):
    if len(ps) < 8:
        raise InvalidPasswordException("Password must contain at least 8 characters")

    if not any(ch.islower() for ch in ps):
        raise InvalidPasswordException("Password must contain a lowercase letter")

    if not any(ch.isupper() for ch in ps):
        raise InvalidPasswordException("Password must contain an uppercase letter")

    if not any(ch.isdigit() for ch in ps):
        raise InvalidPasswordException("Password must contain a digit")
    spcl = "!@#$%^&*()-+"
    if not any(ch in spcl for ch in ps):
        raise InvalidPasswordException("Password must contain a special character")
def validate_login(uname,ps):
    try:
        vali_username(uname)
        vali_password(ps)
        print(f"Welcome '{uname}'")
    except (InvalidUsernameException,InvalidPasswordException) as e:
        print("Invalid username or password.")
        print("Reason:", e)
uname = input("Username: ")
ps = input("Password: ")
validate_login(uname, ps)