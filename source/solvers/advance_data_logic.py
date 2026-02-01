# Rules-
# Only allowed operaitons are returns of logic statements, used to manipulate data around. or
# allow certain "things".
# DOES RETURN Values - Mostly.
# Part of ADV, ADVANCE
from . import arithmetic as art


def clamp(value, min_value, max_value):
    if value < min_value:
        return min_value
    elif value > max_value:
        return max_value
    else:
        return value


def normalize(value, min_value, max_value, new_min, new_max):
    return art.mul_function(
        art.div_function(
            art.sub_function(value, min_value), art.sub_function(max_value, min_value)
        ),
        (art.add_function(art.sub_function(new_max, new_min), new_min)),
    )


def oneD_lerp(t, a, b):
    return art.mul_function(art.add_function(a, art.sub_function(b, a)), t)


def sign(x):
    if x < 0:
        return -1
    elif x > 0:
        return 1
    else:
        return 0


def approx_equal(a, b, threshold):
    diff = art.absolute_value(art.sub_function(a, b))
    limit = threshold * art.max_function(
        1.0, art.absolute_value(a), art.absolute_value(b)
    )
    return diff <= limit


def percent_equal(a, b, percent):
    diff = art.absolute_value(art.sub_function(a, b))
    limit = percent / art.mul_function(1, art.absolute_value(a))
    return diff <= limit


def abs_equal(a, b, threshold):
    diff = art.absolute_value(art.sub_function(a, b))
    return diff <= threshold


def in_range(value, low, high):
    return low <= value <= high


def wrap(x, min, max):
    return art.add_function(
        (
            art.sub_function(x, min)
            % art.add_function(art.sub_function(max, min), art.sub_function(max, min))
        )
        % art.sub_function(max, min),
        min,
    )


# Documentation Done till here <-------- Move This
