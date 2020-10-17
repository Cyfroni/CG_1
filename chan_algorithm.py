from test_manager import test
from data_manager import calc_bottom_hull
from common import getmax_min, compute_upper_tangent, compute_upper_tangent_sorted
from graham_scan import INC_CH
from math import log, floor
import time
import data_manager
import itertools


def split(l, n):
    return [l[i:i + n] for i in range(0, len(l), n)]


def remove_leftmost(p, U):
    new_U = [[v for v in U_i if v.x > p.x] for U_i in U]
    return [U_i for U_i in new_U if len(U_i) > 0]


def tangent(p, U, l):
    t = [compute_upper_tangent(p, l, U_i) for U_i in U]
    t = [pp for pp, rr in t if pp is not None]
    # t = [compute_upper_tangent_sorted(p, U_i) for U_i in U]
    # t = [tt for tt in t if tt is not None]
    return t


def upper_hull(_P):
    n = len(_P)
    p_max, p_min = getmax_min(_P)
    for i in range(1, floor(log(log(n, 2), 2)) + 2):
        h = 2**2**i

        P = split(_P, h)
        U = [INC_CH(P_i, False) for P_i in P]

        _U = []
        p = p_min
        l = 180.0
        for _ in range(h):
            if p == p_max:
                break
            _U.append(p)
            t = tangent(p, U, l)
            p, l = compute_upper_tangent(p, l, t)
            U = remove_leftmost(p, U)

        if p == p_max:
            _U.append(p)
            return _U


def CH_CH(_P):
    hull = upper_hull(_P)
    hull.pop()
    return hull + calc_bottom_hull(upper_hull, _P)


if __name__ == "__main__":
    test(CH_CH, curve_num_points=100)


def compute_upper_tangent_try(p, r, P, min_angle, t, k):
    new_p = None
    new_r = None
    x = 1
    for v in P:
        if p == v:
            continue
        abs_angle = common.calc_angle(p, v)
        rel_angle = common.calc_diff(r, abs_angle)
        if min_angle == rel_angle:
            print("hi")
        if min_angle > rel_angle:
            min_angle = rel_angle
            new_r = abs_angle
            new_p = v
            x = 0
    if (x == 0):
        return new_p, min_angle, new_r,
    else:
        return t, min_angle, k
