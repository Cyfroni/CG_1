from random import random, randint
from points import test
from shapely.geometry import Point


def slope(p1, p2):
    return 1.0 * (p1.y - p2.y) / (p1.x - p2.x) if p1.x != p2.x else float('inf')

def split_by(p, val):
    pl = []
    pr = []

    if len(p)==2:
        x=p[0]
        y=p[1]
        if (x.x<y.x):
            return x,y
        else:
            return y,x

    return separateSets1(p,val)

def separateSets1(points,median):
    pl=[]
    pr=[]
    for x in points:
        if x.x<median.x:
            pl.append(x)
        else:
            pr.append(x)
    return pl,pr

def separateSets(points,left,right):
    pl=[]
    pr=[]
    for x in points:
        if x.x<=left.x:
            pl.append(x)
        elif x.x>=right.x:
            pr.append(x)
    return pl,pr

def separate3Sets(pl, pr, slope,median):
    small=[]
    equal=[]
    big=[]
    smallr=[]
    equalr=[]
    bigr=[]
    for i in range(len(pr)):
        if (slope[i]==median):
            equalr.append(pr[i])
            equal.append(pl[i])
        elif (slope[i]>median):
            bigr.append(pr[i])
            big.append(pl[i])
        else:
            smallr.append(pr[i])
            small.append(pl[i])
    return small,equal,big,smallr,equalr,bigr

def getmax_min(points): # find max and min in n operations
    xmax = Point(-float('Inf'), -float('Inf'))
    xmin = Point(float('Inf'), -float('Inf'))
    for x in points:
        if (x.x<xmin.x):
            xmin=x
        elif(x.x==xmin.x):
            if (x.y>xmin.y):
                xmin=x
        if(x.x>xmax.x):
            xmax = x
        elif (x.x == xmax.x):
            if (x.y > xmax.y):
                xmax = x
    return xmax,xmin

def quickselect(ls, index, lo=0, hi=None, depth=0, fun=lambda e: e):
    if hi is None:
        hi = len(ls)-1
    if lo == hi:
        return ls[lo]
    pivot = randint(lo, hi)
    ls = list(ls)
    ls[lo], ls[pivot] = ls[pivot], ls[lo]
    cur = lo
    for run in range(lo+1, hi+1):
        if fun(ls[run]) < fun(ls[lo]):
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
    canditates=[]

    if len(S) == 2:
        return getmax_min(S)[::-1]

    V = quickselect(S,int( len(S) / 2), fun=lambda e: e.x)

    pl, pr = split_by(S, V)

    if (len(pr)>len(pl)):
        canditates.append(pr.pop(0))
    elif(len(pr)<len(pl)):
        canditates.append(pl.pop(0))

    slopearr = [slope(l, r) for l, r in zip(pl, pr)]

    k = quickselect(slopearr,int(len(slopearr)/2))
    
    max_slope = max(point.y - k * point.x for point in S)
    max_set = [point for point in S if point.y - k * point.x == max_slope]

    msmax, msmin = getmax_min(max_set)
    if msmin.x <= Vl.x < msmax.x:
        return msmin, msmax 
    smalls,equall,bigl,smallr,equalr,bigr=separate3Sets(pl,pr,slopearr,k)

    if Vl.x >= msmax.x:
        canditates.extend(equalr)
        canditates.extend(bigr)
        canditates.extend(smallr)
        canditates.extend(smalls)
    if Vl.x < msmin.x:
        canditates.extend(equall)
        canditates.extend(smalls)
        canditates.extend(bigl)
        canditates.extend(bigr)

    return bridge(canditates,Vl)

def KSHull(points):    
    Vl=quickselect(points,int( len(points) / 2), fun=lambda e: e.x)
    Upl, Upr = bridge(points,Vl)
    Ls,Rs=separateSets(points,Upl,Upr)

    maxs, mins = getmax_min(points)
    if mins == Upl:
        yield Upl
    else:
        yield from KSHull(Ls)

    if maxs == Upr:
        yield Upr
    else:
        yield from KSHull(Rs)

def MbC_CH(points):
    return list(KSHull(points))

if __name__ == "__main__":
    test(MbC_CH)
