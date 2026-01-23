# Rule
# A single fundamental maths function, returning a single value. nothing in between, lists can be count as single vlaue if in loop.
# No hardcoded values or "cheats"


def add_function(*inputs):
    return sum(inputs)


def mul_function(*inputs):
    r = 1
    for x in inputs:
        r *= x
    return r


def sub_function(a, b):
    return a - b


def div_function(a, b):
    return a / b


def exponent_function(a, b):
    return a**b


def sqrt_function(a):
    if a < 0:
        raise ValueError("sqrt requires non-negative input")
    if a == 0:
        return 0
    aproximation = div_function(a, 2)
    for i in range(6):
        aproximation = div_function(
            add_function(aproximation, div_function(a, aproximation)), 2
        )
    return aproximation


def arithmetic_average_mean(*input):
    count = len(input)
    return div_function(add_function(*input), count)


def absolute_value(a):
    if a < 0:
        return mul_function(a, -1)
    elif a > 0:
        return a
    else:
        return 0


def min_function(*input):
    return min(input)


def max_function(*input):
    return max(input)


# Implemented in different-file @random-number-generator.py for import reasons and simplicity
# def random_function(*input):
#    pass


def round_function(a, precision):
    return round(a, precision)


# documentation done till here <- MOVE THIS
