from .. import figs
from ..algorithms import algs as _algs
from ..managers import test_manager as tm, data_manager as dm, plot_manager as pm, experiment_manager as em

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
