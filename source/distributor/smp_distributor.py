from ..solvers import arithmetic as arithmetic

OPS = {
    "add": arithmetic.add_function,
    "mul": arithmetic.mul_function,
    "sub": arithmetic.sub_function,
    "div": arithmetic.div_function,
    "pwr": arithmetic.exponent_function,
    "sqrt": arithmetic.sqrt_function,
    "arithmetic_average": arithmetic.arithmetic_average_mean,
    "abs": arithmetic.absolute_value,
    "min": arithmetic.min_function,
    "max": arithmetic.max_function,
    "round": arithmetic.round_function,
    "distance": arithmetic.distance,
    "receprocal": arithmetic.receprocal,
}


def distribute(type, *data):
    if type not in OPS:
        raise ValueError("Function not found by distributor")
    func = OPS[type]
    return func(*data)
