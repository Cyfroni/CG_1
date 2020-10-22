from .common import getmax_min, quickselect, calc_bottom_hull, orientation
import math


def compare_points(p1, p2):
    return p1.x < p2.x or (p1.x == p2.x and p1.y < p2.y)


def find_median_p(points):
    return quickselect(points, int(len(points) / 2), key=compare_points)


def find_median(values):
    return quickselect(values, int(len(values) / 2))


def slope(p1, p2):
    return 1.0 * (p1.y - p2.y) / (p1.x - p2.x) if p1.x != p2.x else float('inf')


def line(p, a):
    return p.y - a * p.x


def split_by(points, val):
    pl = []
    pr = []
    for p in points:
        if compare_points(p, val):
            pl.append(p)
        else:
            pr.append(p)
    return pl, pr


def separateSets(points, left, right):
    pl = []
    pr = []
    for x in points:
        if x.x < left.x:
            pl.append(x)
        elif x.x > right.x:
            pr.append(x)
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


def bridge(S, Vl):

    if len(S) == 2:
        return getmax_min(S)[::-1]

    pl, pr = split_by(S, find_median_p(S))

    canditates = []
    if (len(pr) > len(pl)):
        canditates.append(pr.pop(0))
    elif(len(pr) < len(pl)):
        canditates.append(pl.pop(0))

    slopearr = []
    i = 0
    while i < len(pl):
        slop = slope(pl[i], pr[i])
        if math.isinf(slop):
            canditates.append(pl[i] if pl[i].y > pr[i].y else pr[i])
            del pl[i]
            del pr[i]
        else:
            slopearr.append(slop)
            i += 1

    k = find_median(slopearr)

    max_slope = max(line(p, k) for p in S)
    max_set = [p for p in S if math.isclose(max_slope, line(p, k))]

    msmax, msmin = getmax_min(max_set)
    if msmin.x <= Vl.x < msmax.x:
        return msmin, msmax

    smalls, equall, bigl, smallr, equalr, bigr = separate3Sets(
        pl, pr, slopearr, k)

    if Vl.x >= msmax.x:
        canditates.extend(equalr)
        canditates.extend(bigr)
        canditates.extend(smallr)
        canditates.extend(smalls)
    elif Vl.x < msmin.x:
        canditates.extend(smalls)
        canditates.extend(equall)
        canditates.extend(bigl)
        canditates.extend(bigr)

    return bridge(canditates, Vl)


def KSHull(S):
    Upl, Upr = bridge(S, find_median_p(S))
    Ls, Rs = separateSets(S, Upl, Upr)
    Ls.append(Upl)
    Rs.append(Upr)

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


def pruning(S, pl, pr):
    return [p for p in S if orientation(pl, p, pr) <= 0]


def KSHull2(S):
    maxs, mins = getmax_min(S)

    S = pruning(S, mins, maxs)
    Upl, Upr = bridge(S, find_median_p(S))
    Ls, Rs = separateSets(S, Upl, Upr)
    Ls.append(Upl)
    Rs.append(Upr)

    if mins == Upl:
        yield Upl
    else:
        yield from KSHull2(Ls)

    if maxs == Upr:
        yield Upr
    else:
        yield from KSHull2(Rs)


def MbC2_CH(P):
    u_hull = list(KSHull2(P))
    b_hull = calc_bottom_hull(KSHull2, P)
    if (u_hull[-1] == b_hull[0]):
        u_hull.pop()
    if (b_hull[-1] == u_hull[0]):
        b_hull.pop()
    return u_hull + b_hull
