# function will convert string parameter to upper case
def to_upper(value):
    if not isinstance(value, str):
        raise TypeError("Input must be a string")
    return value.upper()

# function will check return true if all items on
# the parameter list are upper case
def to_word_list_isupper(str_list):
    if not isinstance(str_list, list):
        raise TypeError("Input must be a list")
    
    for word in str_list:
        if word.islower():
            return False
    return True