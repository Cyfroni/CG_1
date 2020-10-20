from .common import getmax_min, calc_bottom_hull
from random import randint
import math


def compare_points(p1, p2):
    if p1.x < p2.x:
        return True
    elif p1.x == p2.x and p1.y < p2.y:
        return True
    return False


def slope(p1, p2):
    return 1.0 * (p1.y - p2.y) / (p1.x - p2.x) if p1.x != p2.x else float('inf')


def split_by(p, val):
    pl = []
    pr = []

    if len(p) == 2:
        x = p[0]
        y = p[1]
        if compare_points(x, y):
            return x, y
        else:
            return y, x

    return separateSets1(p, val)


def separateSets1(points, median):
    pl = []
    pr = []
    for p in points:
        if compare_points(p, median):
            pl.append(p)
        else:
            pr.append(p)
    return pl, pr


# def separateSets(points, left, right):
#     pl = []
#     pr = []
#     for x in points:
#         if x.x <= left.x:
#             pl.append(x)
#         elif x.x >= right.x:
#             pr.append(x)
#     return pl, pr

def separateSets(points, left, right):
    pl = []
    pr = []
    for p in points:
        if not compare_points(left, p):
            pl.append(p)
        elif not compare_points(p, right):
            pr.append(p)
    return pl, pr


def separate3Sets(pl, pr, slope, median):
    small = []
    equal = []
    big = []
    smallr = []
    equalr = []
    bigr = []
    for i in range(len(slope)):
        if (slope[i] == median):
            equalr.append(pr[i])
            equal.append(pl[i])
        elif (slope[i] > median):
            bigr.append(pr[i])
            big.append(pl[i])
        else:
            smallr.append(pr[i])
            small.append(pl[i])
    return small, equal, big, smallr, equalr, bigr


def quickselect(ls, index, lo=0, hi=None, depth=0, fun=lambda a, b: a < b):
    if hi is None:
        hi = len(ls)-1
    if lo == hi:
        return ls[lo]

    pivot = randint(lo, hi)

    ls = list(ls)
    ls[lo], ls[pivot] = ls[pivot], ls[lo]
    cur = lo
    for run in range(lo+1, hi+1):
        if fun(ls[run], ls[lo]):
            cur += 1
            ls[cur], ls[run] = ls[run], ls[cur]
    ls[cur], ls[lo] = ls[lo], ls[cur]
    if index < cur:
        return quickselect(ls, index, lo, cur-1, depth+1, fun)
    elif index > cur:
        return quickselect(ls, index, cur+1, hi, depth+1, fun)
    else:
        return ls[cur]


def bridge(S, Vl):
    canditates = []

    if len(S) == 2:
        return getmax_min(S)[::-1]

    V = quickselect(S, int(len(S) / 2), fun=compare_points)

    pl, pr = split_by(S, V)

    if (len(pr) > len(pl)):
        # print(">")
        # pl.append(pr[0])
        # print(pl)
        # print(pr)
        canditates.append(pr.pop(0))
    elif(len(pr) < len(pl)):
        # print("<")
        # pr.append(pl[-1])
        canditates.append(pl.pop(0))

    slopearr = [slope(l, r) for l, r in zip(pl, pr)]

    # print(slopearr)

    k = quickselect(slopearr, int(len(slopearr)/2))

    max_slope = max(point.y - k * point.x for point in S)
    max_set = [point for point in S
               if math.isclose(max_slope, point.y - k * point.x)]

    msmax, msmin = getmax_min(max_set)
    if not compare_points(Vl, msmin) and compare_points(Vl, msmax):
        return msmin, msmax
    # try:

    smalls, equall, bigl, smallr, equalr, bigr = separate3Sets(
        pl, pr, slopearr, k)
    # except:
    #     print(pl)
    #     print(pr)
    #     print(slopearr)
    #     print(k)
    #     raise

    if not compare_points(Vl, msmax):
        # if msmax.x <= Vl.x:
        canditates.extend(equalr)
        canditates.extend(bigr)
        canditates.extend(smallr)
        canditates.extend(smalls)
    if compare_points(Vl, msmin):
        # if msmin.x > Vl.x:
        canditates.extend(smalls)
        canditates.extend(equall)
        canditates.extend(bigl)
        canditates.extend(bigr)

    # if msmin.x <= Vl.x > msmax.x:
    #     return msmin, msmax
    # smalls, equall, bigl, smallr, equalr, bigr = separate3Sets(
    #     pl, pr, slopearr, k)
    # if msmax.x <= Vl.x:
    #     canditates.extend(equalr)
    #     canditates.extend(bigr)
    #     canditates.extend(smallr)
    #     canditates.extend(smalls)
    # if msmin.x > Vl.x:
    #     canditates.extend(smalls)
    #     canditates.extend(equall)
    #     canditates.extend(bigl)
    #     canditates.extend(bigr)

    return bridge(canditates, Vl)


def KSHull(S):
    Vl = quickselect(S, int(len(S) / 2), fun=compare_points)
    Upl, Upr = bridge(S, Vl)
    Ls, Rs = separateSets(S, Upl, Upr)
    maxs, mins = getmax_min(S)
    if mins == Upl:
        yield Upl
    else:
        yield from KSHull(Ls)

    if maxs == Upr:
        yield Upr
    else:
        yield from KSHull(Rs)


def MbC_CH(P):
    u_hull = list(KSHull(P))
    b_hull = calc_bottom_hull(KSHull, P)
    if (u_hull[-1] == b_hull[0]):
        u_hull.pop()
    if (b_hull[-1] == u_hull[0]):
        b_hull.pop()
    return u_hull + b_hull
