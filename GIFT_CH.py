from points import random_points_within, points_on, plot, create_circle, create_rect
from shapely.geometry import Point
import math

def get_min(l, key):
    return sorted(l, key=key)[0]

def get_max(l, key):
    return sorted(l, key=key)[-1]

def calc_angle(p1, p2):
    return math.degrees(math.atan2(p2.y-p1.y, p2.x-p1.x))

def getAngle(r, p1, p2):
    ang = r - calc_angle(p1, p2)
    return ang + 360 if ang < 0 else ang

def gift(points):
    points = sorted(points, key= lambda p: p.x)

    hull = []
    q1 = get_min(points, lambda p: p.x)
    p = q1
    r = 180.0
    hull.append(q1)

    a = 5

    cond = True
    while a:
        angles = [(getAngle(r, p, v), v) for v in points if p != v]
        print([a for a, b in angles])
        ang_min = get_min(angles, lambda x: x[0])
        print(ang_min)
        r, p = ang_min
        hull.append(p)

        cond = p != q1
        a -= 1

    return hull

    


if __name__ == "__main__":
    rect = create_rect([(0, 0), (0, 1), (1, 1), (1, 0)])
    points1 = random_points_within(rect, 10)
    hull = gift(points1)
    plot(points1, hull)

    # circle = create_circle(0, 0, 1)
    # points2 = random_points_within(circle)
    # plot(points2, circle)

    # points3 = points_on(lambda x: x*x)
    # plot(points3)
