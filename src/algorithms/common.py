from shapely.geometry import Point
from random import randint
import math


def calc_angle(p1, p2):
    return math.degrees(math.atan2(p2.y-p1.y, p2.x-p1.x))


def calc_diff(r1, r2):
    diff = r1 - r2
    return diff + 360 if diff < 0 else diff


def orientation(p1, p2, p3):  # orientation test add x1y1 -x1y1 to make it easier
    return (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x)


def compute_upper_tangent(p, r, P):
    min_angle = 360
    new_p = None
    new_r = None
    for v in P:
        if p == v:
            continue
        abs_angle = calc_angle(p, v)
        rel_angle = calc_diff(r, abs_angle)
        if min_angle > rel_angle:
            min_angle = rel_angle
            new_r = abs_angle
            new_p = v
    return new_p, new_r


def getmax_min(points):  # find max and min in n operations
    xmax = Point(-float('Inf'), -float('Inf'))
    xmin = Point(float('Inf'), -float('Inf'))
    for x in points:
        if (x.x < xmin.x):
            xmin = x
        elif(x.x == xmin.x):
            if (x.y > xmin.y):
                xmin = x
        if(x.x > xmax.x):
            xmax = x
        elif (x.x == xmax.x):
            if (x.y > xmax.y):
                xmax = x
    return xmax, xmin


def quickselect(ls, index, lo=0, hi=None, key=lambda a, b: a < b):
    if hi is None:
        hi = len(ls)-1
    if lo == hi:
        return ls[lo]

    pivot = randint(lo, hi)

    ls = list(ls)
    ls[lo], ls[pivot] = ls[pivot], ls[lo]
    cur = lo
    for run in range(lo+1, hi+1):
        if key(ls[run], ls[lo]):
            cur += 1
            ls[cur], ls[run] = ls[run], ls[cur]
    ls[cur], ls[lo] = ls[lo], ls[cur]
    if index < cur:
        return quickselect(ls, index, lo, cur-1, key)
    elif index > cur:
        return quickselect(ls, index, cur+1, hi, key)
    else:
        return ls[cur]


def calc_bottom_hull(upper_hull, points):
    inv_p = [Point(-p.x, -p.y) for p in points]
    return [Point(-p.x, -p.y) for p in upper_hull(inv_p)]

# def compute_upper_tangent2(p, P, *args):
#     min2 = P[1]
#     for i in range(2, lenp):
#         p3 = P[i]
#         if p3 == p:
#             continue
#        if orientation(p,min2,P[i])<0:
#            min2=P[i]
#     return min2

# def orientation2(p,  q,  r):
#     val = - ((q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y))
#     if (val == 0):
#         return 0
#     return -1 if (val > 0) else 1

# def compute_upper_tangent_sorted(p, P):
#     l = 0
#     r = len(P)
#     l_before = orientation2(p, P[0], P[-1])
#     l_after = orientation2(p, P[0], P[(l + 1) % len(P)])
#     while (l < r):
#         c = (l + r) // 2
#         c_before = orientation2(p, P[c], P[(c - 1) % len(P)])
#         c_after = orientation2(p, P[c], P[(c + 1) % len(P)])
#         c_side = orientation2(p, P[l], P[c])
#         if c_before != -1 and c_after != -1:
#             return P[c]
#         elif (c_side == 1) and (l_after == -1 or l_before == l_after) or (c_side == -1 and c_before == -1):
#             r = c
#         else:
#             l = c + 1
#         l_before = -c_after
#         l_after = orientation2(p, P[l], P[(l + 1) % len(P)])
#     return P[l]

# def getmax_min1(points):  # find max and min in n operations
#     if (points[0].x > points[1].x):
#         xmax = points[0]
#         xmin = points[1]
#     elif((points[0].x < points[1].x)):
#         xmin = points[0]
#         xmax = points[1]
#     elif(points[0].y > points[1].y):
#         xmin = points[0]
#         xmax = points[0]
#     else:
#         xmax = points[1]
#         xmin = points[1]
#     for x in points[2:-1]:
#         if (x.x < xmin.x):
#             xmin = x
#         elif(x.x > xmax.x):
#             xmax = x
#         elif(x.x == xmin.x):
#             if (x.y > xmin.y):
#                 xmin = x
#         elif (x.x == xmax.x):
#             if (x.y > xmax.y):
#                 xmax = x
#     return xmax, xmin
