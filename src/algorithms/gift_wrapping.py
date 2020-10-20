from .common import getmax_min, compute_upper_tangent


def GIFT_CH(P):
    hull = []
    _, q1 = getmax_min(P)
    p = q1

    hull.append(p)
    r = 180.0

    while True:
        p, r = compute_upper_tangent(p, r, P)
        if p == q1:
            break
        hull.append(p)

    return hull
