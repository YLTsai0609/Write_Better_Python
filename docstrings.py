# you should never have to read the code to figure out what a libray does
def does_something(arg):
    """
    Take one argument and does something based on type
    If arg is a string, return arg * 3
    If arg is an int or float, return arg * 10
    """
    if isinstance(arg, (int, float)):
        return arg + 10
    elif isinstance(arg, str):
        return str * 3
    else:
        raise TypeError("does_something only takes ints, floats, and strings")
