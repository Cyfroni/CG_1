from .common import getmax_min, calc_bottom_hull
from random import randint
import math
from ..managers import plot_manager as pm
from shapely.geometry import Point
from operator import attrgetter

print = lambda *args: None


def pp(name, p):
    print(name, *sorted(p, key=attrgetter("x", "y")))


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
        if (x.x < y.x):
            return [x], [y]
        else:
            return [y], [x]

    if len(p) % 2 == 0:
        return separateSets1(p, val)
    else:
        # return separateSets2(p, val)
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


def separateSets2(points, median):
    pl = []
    pr = []
    pl.append(median)
    for p in points:
        if p == median:
            continue
        elif compare_points(p, median):
            pl.append(p)
        else:
            pr.append(p)
    pr.append(median)
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

# def separateSets(points, left, right):
#     pl = []
#     pr = []
#     for p in points:
#         if not compare_points(left, p):
#             pl.append(p)
#         elif not compare_points(p, right):
#             pr.append(p)
#     return pl, pr


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
    # S = SS[:]
    canditates = []
    if len(S) == 2:
        return getmax_min(S)[::-1]

    # if len(S) % 2 == 1:
    #     canditates.append(S.pop())

    print("q - 1", len(S))
    V = quickselect(S, int(len(S) / 2), fun=compare_points)

    pl, pr = split_by(S, V)

    pp("S", S)
    pp("pl", pl)
    pp("pr", pr)
    pp("V", [V])
    pp("Vl", [Vl])
    # print("pl", *pl)
    # print("pr", *pr)
    # print("V", V)

    if (len(pr) > len(pl)):
        canditates.append(pr.pop(0))
    elif(len(pr) < len(pl)):
        canditates.append(pl.pop(0))

    assert len(pl) == len(pr)

    slopearr = []
    i = 0
    while True:
        sl = slope(pl[i], pr[i])
        if math.isinf(sl):
            print("cand", *canditates)
            canditates.append(max(pl[i], pr[i], key=lambda x: x.y))
            print("cand2", *canditates)
            print("plr", *pl, *pr)
            del pl[i]
            del pr[i]
            print("plr2", *pl, *pr)
        else:
            slopearr.append(sl)
            i += 1

        if (i >= len(pl)):
            break

    # if len(slopearr) == 0:
    #     assert len(canditates) > 1
    #     print("############", len(canditates))
    #     return bridge(canditates, Vl)

    print("q - 2", len(slopearr))
    k = quickselect(slopearr, int(len(slopearr)/2))

    max_slope = max(point.y - k * point.x for point in S)
    max_set = [point for point in S
               if math.isclose(max_slope, point.y - k * point.x)]
    pp("max_set", max_set)
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
    else:
        print('else: ', Vl)

    return bridge(canditates, Vl)


def KSHull(S):
    print("q - 3", len(S))
    Vl = quickselect(S, int(len(S) / 2), fun=compare_points)
    # pm.plot(S, [], [Point([0, 0]), Vl])
    Upl, Upr = bridge(S, Vl)
    print("S: ", *S)
    print("Bridge: ", Upl, Upr)
    Ls, Rs = separateSets(S, Upl, Upr)
    Ls.append(Upl)
    Rs.append(Upr)
    maxs, mins = getmax_min(S)
    if mins == Upl:
        print("mins", mins)
        yield Upl
    else:
        print("Ls")
        print(*Ls)
        print(Upl)
        yield from KSHull(Ls)

    if maxs == Upr:
        print("maxs", maxs)
        yield Upr
    else:
        print("Rs")
        print(*Rs)
        print(Upr)
        yield from KSHull(Rs)


def MbC_CH(P):
    u_hull = list(KSHull(P))
    b_hull = calc_bottom_hull(KSHull, P)
    if (u_hull[-1] == b_hull[0]):
        u_hull.pop()
    if (b_hull[-1] == u_hull[0]):
        b_hull.pop()
    return u_hull + b_hull
