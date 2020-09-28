from random import random, randint
from points import test
from shapely.geometry import Point


def slope(p1, p2):
    return 1.0 * (p1.y - p2.y) / (p1.x - p2.x) if p1.x != p2.x else float('inf')
def MbC_CH(points):
    Vl=quickselectP(points,int( len(points) / 2))
    UpL,Upr=bridge(points,Vl)
    points=removepointsbelowbridge(points,UpL,Upr)
    Ls,Rs=separateSets(points,UpL,Upr)
    return MbC_CH(Ls)+MbC_CH(Rs)

def bridge(Set, Vl):
    canditates=[]
    pr=[]
    pl=[]
    slopearr=[]
    print(len(Set))
    if len(Set)==2:
        x=Set.pop()
        y=Set.pop()
        if (x.x<y.x):
            return x,y
        else:
            return y,x
    while(len(pr)-len(pl)>1 or len(pl)-len(pr)>1 or len(pr)==0):
        pr,pl=separateSets1(Set,Vl)
    print(len(pr), len(pl))
    if (len(pr)>len(pl)):
        canditates.append(pr.pop(0))
    elif(len(pr)<len(pl)):
        canditates.append(pl.pop(0))
    print(len(pr),len(pl))
    for i in range(len(pr)):
        if (pr[i].x!=pl[i].x):
            slopearr.append(slope(pl[i],pr[i]))
        else:
            canditates.append(pr[i] if pr[i].y > pl[i].y else pl[i])
            pr.pop(i)
            pl.pop(i)
            print("hi")
        #if (pr[i].x==pl[i].x):
           # canditates.add(pr[i] if pr[i].y > pl[i].y else pl[i])
            #pr.pop(i)
          #  pl.pop(i)
       # else:
          #  slopearr[i]=calslope(pr[i],pl[i])
    median_index = len(slopearr)
    print(median_index)
    k=quickselect(slopearr,int(median_index/2))
    max_slope = max(point.y - k * point.x for point in Set)
    max_set = [point for point in Set if point.y - k * point.x == max_slope]
    msmin, msmax = getmax_min(max_set)
    if msmin.x <= Vl.x and msmax.x > Vl.x:
        return msmin, msmax
    smalls,equall,bigl,smallr,equalr,bigr=separate3Sets(pr,pl,slopearr,k)

    if msmax.x <= Vl.x:
        canditates.extend(equalr)
        canditates.extend(bigr)
        canditates.extend(smallr)
        canditates.extend(smalls)
    if msmin.x > Vl.x:
        canditates.extend(equall)
        canditates.extend(smalls)
        canditates.extend(bigl)
        canditates.extend(bigr)
    if (len(canditates) % 2==1):
        canlen=int(len(canditates) / 2)+1
    else:
        canlen = len(canditates) / 2

    Vl = quickselectP(canditates, canlen)
    return bridge(canditates,Vl)

def separateSets1(points,median):
    pr=[]
    pl=[]
    for x in points:
        if x.x<median.x:
            pl.append(x)
        else:
            pr.append(x)
    return pr,pl

def separateSets(points,left,right):
    pr=[]
    pl=[]
    for x in points:
        if x.x<=left.x:
            pl.append(x)
        elif x.x>right.x:
            pr.append(x)
    return pr,pl
def separate3Sets(pr,pl,slope,median):
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


def quickselect(ls, index, lo=0, hi=None, depth=0):
    if hi is None:
        hi = len(ls)-1
    if lo == hi:
        return ls[lo]
    pivot = randint(lo, hi)
    ls = list(ls)
    ls[lo], ls[pivot] = ls[pivot], ls[lo]
    cur = lo
    for run in range(lo+1, hi+1):
        if ls[run] < ls[lo]:
            cur += 1
            ls[cur], ls[run] = ls[run], ls[cur]
    ls[cur], ls[lo] = ls[lo], ls[cur]
    if index < cur:
        return quickselect(ls, index, lo, cur-1, depth+1)
    elif index > cur:
        return quickselect(ls, index, cur+1, hi, depth+1)
    else:
        return ls[cur]

def quickselectP(ls, index, lo=0, hi=None, depth=0):
    if hi is None:
        hi = len(ls)-1
    if lo == hi:
        return ls[lo]
    pivot = randint(lo, hi)
    ls = list(ls)
    ls[lo], ls[pivot] = ls[pivot], ls[lo]
    cur = lo
    for run in range(lo+1, hi+1):
        if ls[run].x < ls[lo].x:
            cur += 1
            ls[cur], ls[run] = ls[run], ls[cur]
    ls[cur], ls[lo] = ls[lo], ls[cur]
    if index < cur:
        return quickselectP(ls, index, lo, cur-1, depth+1)
    elif index > cur:
        return quickselectP(ls, index, cur+1, hi, depth+1)
    else:
        return ls[cur]
def removepointsbelowbridge(points,pointl,pointr):
    for i in (points):
        if (i.x>pointl.x and i.x<pointr.x ):
            points.remove(i)
    return points


def getmedian(xmax,xmin):
    return (xmax.x+xmin.x)/2


test(MbC_CH)
