from data_manager import test, calc_bottom_hull
from common import getmax_min, compute_upper_tangent
from graham_scan import INC_CH
from math import log, floor


def split(l, n):
    return [l[i:i + n] for i in range(0, len(l), n)]


def remove_leftmost(p, U):
    new_U = [[v for v in U_i if v.x > p.x] for U_i in U]
    return [U_i for U_i in new_U if len(U_i) > 0]


def upper_hull(_P):
    n = len(_P)
    p_max, p_min = getmax_min(_P)
    for i in range(1, floor(log(log(n, 2), 2)) + 2):
        h = 2**2**i
        P = split(_P, h)
        U = [INC_CH(P_i) for P_i in P]
        _U = []

        p = p_min
        l = 180.0
        for _ in range(h):
            _U.append(p)
            if p == p_max:
                break
            t = [compute_upper_tangent(p, l, U_i) for U_i in U]
            t = [pp for pp, rr in t if pp is not None]
            p, l = compute_upper_tangent(p, l, t)
            U = remove_leftmost(p, U)
        if p == p_max:
            return _U


def CH_CH(_P):
    return upper_hull(_P) + calc_bottom_hull(upper_hull, _P)


if __name__ == "__main__":
    test(CH_CH, curve_num_points=100)
