###Decorator functions for one through nine
def zero(function = None, *args)->int:
    return function(0, *args) if function else 0

def one(function = None, *args):
    return function(1, *args) if function else 1 

def two(function = None, *args):
    return function(2, *args) if function else 2

def three(function = None, *args):
    return function(3, *args) if function else 3

def four(function = None, *args):
    return function(4, *args) if function else 4


def five(function = None, *args):
    return function(5, *args) if function else 5


def six(function = None, *args):
    return function(6, *args) if function else 6

def seven(function = None, *args):
    return function(7, *args) if function else 7

def eight(function = None, *args):
    return function(8, *args) if function else 8

def nine(function = None, *args):
    return function(9, *args) if function else 9

def plus(val):
    return lambda x: x + val

def minus(val):
    return lambda x: x - val

def times(val):
    return lambda x: x * val

def divided_by(val):
    return lambda x: x // val


if __name__ in "__main__":
    four(plus(nine()))