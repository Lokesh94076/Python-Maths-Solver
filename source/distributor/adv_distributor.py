from ..solvers import advance_data_logic as adv_d_l

OPS = {
    "clamp": adv_d_l.clamp,
    "normalize": adv_d_l.normalize,
    "1D_lerp": adv_d_l.oneD_lerp,
}


def distribute(type, *data):
    if type not in OPS:
        raise ValueError("Function not found by distributor")
    func = OPS[type]
    return func(*data)
