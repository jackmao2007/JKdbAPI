import mysql.connector


def is_valid_password(paswd: str) -> bool:
    """ check if paswd is a valid password

    password is valid if:

    0. at least 8 characters long
    1. Contains one lowercase letter
    2. Contains one capital letter
    3. Contains one number
    4. Contains a spacial character
    """
    crt = [False, False, False, False, False]
    for char in paswd:
        
