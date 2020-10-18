from graham_scan import INC_CH
from gift_wrapping import GIFT_CH
from chan_algorithm import CH_CH
from marriage_before_conquest import MbC_CH
from test_manager import run
import math


if __name__ == "__main__":
    pi = math.pi
    sqrt10 = math.sqrt(10)
    creds = [
        [(0, 0), (0, 1), (1, 1), (1, 0)],
        [(0, 0), (0, sqrt10), (sqrt10, sqrt10), (sqrt10, 0)],
        [(0, 0), (0, 10), (10, 10), (10, 0)],
        [(0, 0), (0, 10*sqrt10), (10*sqrt10, 10*sqrt10), (10*sqrt10, 0)],
        [(0, 0), (0, 100), (100, 100), (100, 0)],
        [0, 0, 1/pi],
        [0, 0, sqrt10/pi],
        [0, 0, 10/pi],
        [0, 0, 10*sqrt10/pi],
        [0, 0, 100/pi],
        # (lambda x: -x*x, (-1, 1))
    ]

    num_points = [
        10,
        100,
        1000,
        10000,
        100000
    ]

    algs = [
        INC_CH,
        GIFT_CH,
        CH_CH,
        MbC_CH
    ]

    run(creds, num_points, algs, filename="Res1", iterations=10, view=True)
