
######  BOOLEAN DATA VALIDATION

def is_bool(obj):
    return isinstance(obj, bool)

def error_not_bool(obj, ref="Object"):
    if not isinstance(obj, bool):
        raise TypeError(f"{repr(ref)} must be 'True' or 'False'!")

def try_string_to_bool(string):
    truthy_strings = ("true", "t", "1")
    falsy_strings = ("false", "f", "0")

    if string in truthy_strings:
        return True
    if string in falsy_strings:
        return False

    return string

######  STRING DATA VALIDATION

def is_string(obj):
    return isinstance(obj, str)

def error_not_string(obj, ref="Object"):
    if not isinstance(obj, str):
        raise TypeError(f"{repr(ref)} must be a string!")

def is_empty_string(obj):
    return obj == ""

######  INTEGER DATA VALIDATION

def is_int(obj):
    return isinstance(obj, int)

def error_not_int(obj, ref="Object"):
    if not isinstance(obj, int):
        raise TypeError(f"{repr(ref)} must be an integer!")
