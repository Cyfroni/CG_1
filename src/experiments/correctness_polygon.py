from . import _algs, _creds, _num_points, tm, dm, pm
from .helpers import assert_sameness
import random

_creds = _creds[:-1]
_num_points = _num_points[:2]


def run(algs=_algs, creds=_creds, num_points=_num_points):
    print("\n\nCORRECTNESS_POLYGON\n")
    i = 1
    end = len(creds) * len(num_points)
    for cred in creds:
        for num in num_points:
            points, fig = dm.gen_points(cred, num)
            fig_p = pm.unzip_fig(fig)
            points += fig_p
            random.shuffle(points)
            res = [tm.run_alg(alg, points) for alg in algs]
            hulls = [hull for hull, _ in res]

            assert_sameness(hulls, fig_p)

            print(f"({i}/{end})")
            i += 1
    print("\n\nCORRECTNESS_POLYGON: PASSED\n")
