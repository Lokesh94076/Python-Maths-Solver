from ..solvers import advance_data_logic as advance

OPS = {
    "clamp": advance.clamp,
    "normalize": advance.normalize,
    "1d_lerp": advance.oneD_lerp,
    "sign": advance.sign,
    "abs_equal": advance.abs_equal,
    "apx_eql": advance.approx_equal,
    "percent_equal": advance.percent_equal,
    "in_range": advance.in_range,
    "wrap": advance.wrap,
}


def distribute(type, *data):
    if type not in OPS:
        raise ValueError("Function not found by distributor")
    func = OPS[type]
    return func(*data)
