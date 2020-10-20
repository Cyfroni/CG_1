from . import _algs, _creds, _num_points, tm, dm, pm
from .helpers import assert_sameness
from operator import attrgetter


def run(algs=_algs, creds=_creds, num_points=_num_points):
    print("\n\nCORRECTNESS_POLYGON\n")
    i = 1
    end = len(creds) * len(num_points)
    for cred in creds:
        for num in num_points:
            print(f"({i}/{end})")

            points, fig = dm.gen_points(cred, num)
            fig_p = pm.unzip_fig(fig)
            points += fig_p
            res = [tm.run_alg(alg, points) for alg in algs]
            hulls = [hull for hull, _ in res]
            try:
                assert_sameness(hulls, fig_p)
            except:
                for hull in hulls:
                    print(len(hull))
                    print(*sorted(hull, key=attrgetter("x", "y")))
                    pm.plot(points, hull)

            i += 1
    print("\n\nCORRECTNESS_POLYGON: PASSED\n")
