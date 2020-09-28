from points import test
from Marriage_before_Conquest import getmax_min 
import math

def calc_angle(p1, p2):
    return math.degrees(math.atan2(p2.y-p1.y, p2.x-p1.x))

def calc_diff(r1, r2):
    diff = r1 - r2 
    return diff + 360 if diff < 0 else diff

def compute_upper_tangent(p, r, P):
    min_angle = 360
    new_p = None
    new_r = None
    for v in P:
        if p == v: continue
        abs_angle = calc_angle(p, v)
        rel_angle = calc_diff(r, abs_angle)
        if min_angle > rel_angle:
            min_angle = rel_angle
            new_r = abs_angle
            new_p = v
    return new_p, new_r

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
