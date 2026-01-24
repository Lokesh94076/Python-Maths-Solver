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


# Documentation Done till here <-------- Move This
