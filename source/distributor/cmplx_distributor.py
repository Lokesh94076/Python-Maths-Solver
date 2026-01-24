from ..solvers import random_number_generator as rng

OPS = {
    "random-int": rng.generate_random,
    "random": rng.generate_random_ninp,
}


def distribute(type, *data):
    if type not in OPS:
        raise ValueError("Function not found by distributor")
    func = OPS[type]
    return func(*data)
