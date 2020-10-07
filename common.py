from shapely.geometry import Point
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
