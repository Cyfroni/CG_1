from test_manager import test
from data_manager import calc_bottom_hull
from common import getmax_min, compute_upper_tangent, compute_upper_tangent_sorted
from graham_scan import INC_CH
from math import log, floor
import time
import data_manager
import itertools


def split(l, n):
    # start = time.time()
    res = [l[i:i + n] for i in range(0, len(l), n)]
    # print(time.time() - start)
    return res


def remove_leftmost(p, U):
    new_U = [[v for v in U_i if v.x > p.x] for U_i in U]
    return [U_i for U_i in new_U if len(U_i) > 0]


def upper_hull(_P):
    n = len(_P)
    p_max, p_min = getmax_min(_P)
    for i in range(1, floor(log(log(n, 2), 2)) + 2):
        h = 2**2**i
        P = split(_P, h)
        # print(len(_P))
        # print(len(_P[0]))
        # start = time.time()
        U = [INC_CH(P_i) for P_i in P]
        # print(time.time() - start)
        _U = []
        p = p_min
        l = 180.0
        # start = time.time()
        for _ in range(h):
            _U.append(p)
            if p == p_max:
                break
            # start = time.time()
            t = [compute_upper_tangent(p, l, U_i) for U_i in U]
            t = [pp for pp, rr in t if pp is not None]
            # t = [compute_upper_tangent_sorted(p, U_i) for U_i in U]
            # t = [tt for tt in t if tt is not None]
            # print(t)
            # print(len(t))
            # print(t[0])
            # print("#: ", time.time() - start)
            # start = time.time()
            # data_manager.plot(list(itertools.chain.from_iterable(U)))
            p, l = compute_upper_tangent(p, l, t)
            U = remove_leftmost(p, U)
            # data_manager.plot(t, _U + [p])
            # print(time.time() - start)
        # print(time.time() - start)
        if p == p_max:
            return _U


def CH_CH(_P):
    return upper_hull(_P)  # + calc_bottom_hull(upper_hull, _P)


if __name__ == "__main__":
    test(CH_CH, curve_num_points=100)
