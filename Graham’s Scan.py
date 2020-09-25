from typing import List

import points
import random
import matplotlib.pyplot as plt
from shapely.geometry import Polygon, Point
def INCCH (pointsA: List[Point]) -> List[Point]:

    def orientation(p1, p2, p3):  # orientation test add x1y1 -x1y1 to make it easier
        return (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x)
    points = []
    pointsB=sorted(pointsA, key=lambda p: (p.x, p.y))
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
    Upans.append(pointsB[0])
    pointsB.pop(0)
    for p in pointsB:
        Lowans.append(p)
        while len(Lowans) > 2 and orientation(Lowans[-3], Lowans[-2], Lowans[-1]) < 0:
            Lowans.pop(-2)
    Lowans.append(Upans)
    return Lowans

rect = points.create_rect([(0, 0), (0, 1), (1, 1), (1, 0)])
points1 = points.random_points_within(rect)
#points.plot(points1, None, rect)
test=INCCH(points1)
points.plot(test, None, rect)

