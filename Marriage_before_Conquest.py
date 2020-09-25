from typing import List
import numpy as np
from points import random_points_within, points_on, plot, create_circle, create_rect
import random
import matplotlib.pyplot as plt
from shapely.geometry import Polygon, Point


def slope(p1, p2):
    return 1.0 * (p1.y - p2.y) / (p1.x - p2.x) if p1.x != p2.x else float('inf')
def MbC_CH(points):
    pass
def bridge(x,y):
    pass
def separateSets(points,median):
    pr=[]
    pl=[]
    for x in points:
        if x.x<median:
            pl.append(x)
        else:
            pr.append(x)

def getmax_min(points): # find max and min in n operations
    xmax=Point(-np.inf, -np.inf)
    xmin = Point(np.inf, -np.inf)
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

def getmedian(xmax,xmin):
    return (xmax.x+xmin.x)/2

