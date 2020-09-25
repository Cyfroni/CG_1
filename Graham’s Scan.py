from typing import List

from points import random_points_within, points_on, plot, create_circle, create_rect
import random
import matplotlib.pyplot as plt
from shapely.geometry import Polygon, Point
def INCCH (pointsA):

    def orientation(p1, p2, p3):  # orientation test add x1y1 -x1y1 to make it easier
        return (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x)
    points = []
    #pointsB=sorted(pointsA, key=lambda p: (p.x, p.y))
    pointsB = sorted(pointsA, key=lambda p: (p.x))
    Upans=[]
    Lowans=[]
    ans=[]
    Upans.append(pointsB[0])
    temp=pointsB[0]
    pointsB.pop(0)
    for p in pointsB:
        Upans.append(p)
        while len(Upans) > 2 and orientation(Upans[-3], Upans[-2], Upans[-1]) < 0:
            Upans.pop(-2)
    pointsB.insert(0,temp)
    pointsB.reverse() #if reverse takes time, we can iterate with index from last to first
    Lowans.append(pointsB[0])
    pointsB.pop(0)

    for p in pointsB:
        Lowans.append(p)
        while len(Lowans) > 2 and orientation(Lowans[-3], Lowans[-2], Lowans[-1]) < 0:
            Lowans.pop(-2)
    Upans.extend(Lowans)
    #return Lowans,Upans
    return Upans

rect = create_rect([(0, 0), (0, 1), (1, 1), (1, 0)])
points1 = random_points_within(rect,100000)
test=INCCH(points1)
plot(points1, (test))

circle = create_circle(0, 0, 1)
points2 = random_points_within(circle)
test2=INCCH(points2)
plot(points2, test2, circle)

points3 = points_on(lambda x: x * x)
test2=INCCH(points3)
plot(points3,test2)

