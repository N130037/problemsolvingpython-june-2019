#Function to add contact to contact text file

import re

def phonenumbervalidator(number):
    pattern='^[6-9][0-9]{9}$|^[0][6-9][0-9]{9}$|^[+][9][1][6-9][0-9]{9}$'
    if re.match(pattern,str(number)):
        return True
    return False


def emailvalidator(email):
    pattern='^[0-9a-z][0-9a-z_.]{4,13}[0-9a-z][@][0-9a-z]{3,18}[.][a-z]{2,4}|[.][a-z]{2,4}$'
    if re.match(pattern,email):
        return True
    return False
