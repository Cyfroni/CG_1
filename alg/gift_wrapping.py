from data_manager import test
from common import getmax_min, compute_upper_tangent


def GIFT_CH(P):
    hull = []
    _, q1 = getmax_min(P)
    p = q1
    r = 180.0
    hull.append(q1)

    cond = True
    while cond:
        p, r = compute_upper_tangent(p, r, P)
        hull.append(p)
        cond = p != q1

    return hull


if __name__ == "__main__":
    test(GIFT_CH, curve_num_points=100)