from graham_scan import INC_CH
from gift_wrapping import GIFT_CH
from chan_algorithm import CH_CH
from marriage_before_conquest import MbC_CH
from test_manager import run, test
import math

pi = math.pi
sqrt10 = math.sqrt(10)


def xx_c(area):
    b = (1.5*area) ** (1/3)
    return (lambda x: -x*x, (-b, b))


def disc_c(area):
    r_2 = area / (pi/8 - math.sin(pi/8) * math.cos(pi/8))
    a = math.sqrt(r_2) * math.sin(pi/8)
    return (lambda x: math.sqrt(r_2 - x*x), (-a, a))


if __name__ == "__main__":

    creds = [
        # Rectangle
        [(0, 0), (0, 1), (1, 1), (1, 0)],
        [(0, 0), (0, sqrt10), (sqrt10, sqrt10), (sqrt10, 0)],
        [(0, 0), (0, 10), (10, 10), (10, 0)],
        [(0, 0), (0, 10*sqrt10), (10*sqrt10, 10*sqrt10), (10*sqrt10, 0)],
        [(0, 0), (0, 100), (100, 100), (100, 0)],

        # Circle
        [0, 0, 1/pi],
        [0, 0, sqrt10/pi],
        [0, 0, 10/pi],
        [0, 0, 10*sqrt10/pi],
        [0, 0, 100/pi],

        # -x^2 curve
        xx_c(1),
        xx_c(10),
        xx_c(100),
        xx_c(1000),
        xx_c(10000),

        # Disc curve
        disc_c(1),
        disc_c(10),
        disc_c(100),
        disc_c(1000),
        disc_c(10000),

        # Point curve
        # ((-1, 1), lambda x: -x*x)
    ]

    num_points = [
        10,
        100,
        1000,
        10000,
        # 100000
    ]

    algs = [
        INC_CH,
        GIFT_CH,
        CH_CH,
        MbC_CH
    ]

    run(creds, num_points, algs, filename="Res", iterations=10)
    # [test(alg) for alg in algs]
