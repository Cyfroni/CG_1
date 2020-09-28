from points import test
import points
from Marriage_before_Conquest import getmax_min
from graham_scan import INCCH
from GIFT_CH import compute_upper_tangent, calc_diff
from math import log, floor, ceil

def split(l, n):
    return [l[i:i + n] for i in range(0, len(l), n)]

def find_smallest_angle(t, l):
    new_p = None
    new_r = 360.0
    for p, r in t:
        diff = calc_diff(l, r)
        if diff < new_r:
            new_r = r
            new_p = p
    return new_p, new_r

def remove_leftmost(p, U):
    new_U =  [ [v for v in U_i if v.x > p.x] for U_i in U ]
    return [ U_i for U_i in new_U if len(U_i) > 0 ]

def chan(_P):
    n = len(_P)
    __U = []
    p_max, p_min = getmax_min(_P)
    for i in range(1, floor(log(log(n, 2), 2))):
        h = 2**2**(i+1)
        # m = n / h
        P = split(_P, h)
        U = [INCCH(P_i) for P_i in P]
        _U = []
        
        # for p, u in zip (P, U):
        #     points.plot(p, u)

        p = p_min
        l = 180.0
        for _ in range(h):
            _U.append(p)
            print(_U)
            points.plot(_P, _U)
            if p == p_max:
                break
            t = [compute_upper_tangent(p, l, U_i) for U_i in U]
            print(t)
            t = [t_i for t_i in t if t_i[0] is not None]
            # print(t)
            p, l = find_smallest_angle(t, l)
            print(p, l)
            U = remove_leftmost(p, U)
            # for pp, uu in zip (P, U):
            #     points.plot(pp, uu)
        if p == p_max:
            __U = _U
        
        # points.plot(_P, _U)
    return __U

if __name__ == "__main__":
    fig = points.create_fig([0, 0, 1])
    p = points.random_points_within(fig, 2**2**3 - 100) # / 2**2**2 = 9.75 => 10 rounds
    hull = chan(p)
    # points.plot(p, hull)
    # test(chan, curve_num_points=100)
