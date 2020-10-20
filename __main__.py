from src.algorithms import INC_CH, GIFT_CH, CH_CH, MbC_CH
from src.experiments import correctness, correctness_polygon, correctness_visual, exp1_size, exp2_shape
from src.managers import experiment_manager as em
from src import figs
import math


def main():
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
        # (lambda x: -x*x, (-1, 1)),
        ((-1, 1), lambda x: -x*x)
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

    em.run(algs, creds, num_points, filename="Res_",
           iterations=10, view=True, timeout=10)


if __name__ == "__main__":
    # correctness.run()
    # correctness_polygon.run()
    # correctness_visual.run()
    main()
    # exp1_size.run()
    # exp2_shape.run()
