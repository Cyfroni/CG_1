from test_manager import test


def orientation(p1, p2, p3):  # orientation test add x1y1 -x1y1 to make it easier
    return (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x)


def INC_CH(pointsA):
    points = []
    pointsB = sorted(pointsA, key=lambda p: (p.x))
    Upans = []
    Lowans = []
    ans = []
    Upans.append(pointsB[0])
    temp = pointsB[0]
    pointsB.pop(0)
    for p in pointsB:
        Upans.append(p)
        while len(Upans) > 2 and orientation(Upans[-3], Upans[-2], Upans[-1]) < 0:
            Upans.pop(-2)
    pointsB.insert(0, temp)
    pointsB.reverse()  # if reverse takes time, we can iterate with index from last to first
    Lowans.append(pointsB[0])
    pointsB.pop(0)

    for p in pointsB:
        Lowans.append(p)
        while len(Lowans) > 2 and orientation(Lowans[-3], Lowans[-2], Lowans[-1]) < 0:
            Lowans.pop(-2)
    Upans.extend(Lowans)
    return Upans


if __name__ == "__main__":
    test(INC_CH, curve_num_points=100)
