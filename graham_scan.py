from test_manager import test
from common import orientation


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
    Upans.pop()
    pointsB.insert(0, temp)
    pointsB.reverse()  # if reverse takes time, we can iterate with index from last to first
    Lowans.append(pointsB[0])
    pointsB.pop(0)

    for p in pointsB:
        Lowans.append(p)
        while len(Lowans) > 2 and orientation(Lowans[-3], Lowans[-2], Lowans[-1]) < 0:
            Lowans.pop(-2)
    Lowans.pop()
    # Upans.extend(Lowans)
    return Upans + Lowans


if __name__ == "__main__":
    test(INC_CH, curve_num_points=100)
