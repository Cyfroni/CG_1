from src.algorithms import INC_CH, GIFT_CH, CH_CH, MbC_CH, MbC2_CH
from src.experiments import correctness, correctness_polygon, correctness_visual, exp1_size_c, exp2_area_c, exp3_hull
from src.managers import experiment_manager as em
from src import figs
import math


def main():
    _creds = [
        # Rectangle
        figs.rect(1),
        figs.rect(10),
        figs.rect(100),
        figs.rect(1000),
        figs.rect(10000),

        # Circle
        figs.circle(1),
        figs.circle(10),
        figs.circle(100),
        figs.circle(1000),
        figs.circle(10000),

        # -x^2 curve
        figs.xx_c(1),
        figs.xx_c(10),
        figs.xx_c(100),
        figs.xx_c(1000),
        figs.xx_c(10000),

        # Disc curve
        figs.disc_c(1),
        figs.disc_c(10),
        figs.disc_c(100),
        figs.disc_c(1000),
        figs.disc_c(10000),

        # Point curve
        ((-1, 1), lambda x: -x*x)
    ]

    _num_points = [
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
        MbC_CH,
        MbC2_CH,
    ]

    em.run(algs, creds, num_points, filename="res_main",
           iterations=10, view=True, timeout=200)


if __name__ == "__main__":
    # correctness.run()
    # correctness_polygon.run()
    # correctness_visual.run()
    # main()
    exp3_hull.run()
    exp1_size_c.run()
    # exp2_area_c.run()
