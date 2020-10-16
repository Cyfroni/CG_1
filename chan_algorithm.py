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
    # def split(*args): return []
    # def INC_CH(*args): return []
    # def tangent(*args): return []
    # def compute_upper_tangent(*args): return [1, 2]
    # def remove_leftmost(*args): return []
    for i in range(1, floor(log(log(n, 2), 2)) + 2):
        h = 2**2**i

        # start = time.time()
        P = split(_P, h)
        # print(f"[{i}]split: {time.time() - start}")

        # start = time.time()
        U = [INC_CH(P_i, False) for P_i in P]
        # print(f"[{i}]grahams: {time.time() - start}")

        _U = []
        p = p_min
        l = 180.0
        # start = time.time()
        for ii in range(h):
            _U.append(p)
            if p == p_max:
                break

            # start = time.time()
            t = tangent(p, U, l)
            # print(f"[{i}][{ii}]tangent: {time.time() - start}")

            # data_manager.plot(list(itertools.chain.from_iterable(U)))

            # start = time.time()
            p, l = compute_upper_tangent(p, l, t)
            # print(f"[{i}][{ii}]tangent2: {time.time() - start}")

            # start = time.time()
            U = remove_leftmost(p, U)
            # print(f"[{i}][{ii}]remove: {time.time() - start}")

        # print(f"[{i}]end: {time.time() - start}")
        if p == p_max:
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
