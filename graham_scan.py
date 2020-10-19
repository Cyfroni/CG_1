from test_manager import test
from common import orientation


def upper_hull(sorted_P):
    ans = []
    for p in sorted_P:
        ans.append(p)
        if p == sorted_P[0]:
            continue
        while len(ans) > 2 and orientation(ans[-3], ans[-2], ans[-1]) < 0:
            ans.pop(-2)
    return ans


def INC_CH(points, full=True):
    P = sorted(points, key=lambda p: -(p.x))
    hull = upper_hull(P)

    if full:
        hull.pop()
        P.reverse()
        hull = hull + upper_hull(P)
    return hull


if __name__ == "__main__":
    test(INC_CH)
