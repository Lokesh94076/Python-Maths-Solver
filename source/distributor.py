from .solvers import advance_data_logic as adv_d_l
from .solvers import arithmetic as arithmetic
from .solvers import random_number_generator as rng

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
    "random-int": rng.generate_random,
    "random": rng.generate_random_ninp,
    "round": arithmetic.round_function,
    "clamp": adv_d_l.clamp,
    "normalize": adv_d_l.normalize,
    "1D_lerp": adv_d_l.oneD_lerp,
    "distance": arithmetic.distance,
}


def distribute(type, *data):
    if type not in OPS:
        raise ValueError("Function not found by distributor")
    func = OPS[type]
    return func(*data)
