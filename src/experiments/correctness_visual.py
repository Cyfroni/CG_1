from . import _algs, tm, pm


def test_alg_default(alg,
                     poly=[(0, 0), (0, 1), (1, 1), (1, 0)], poly_num_points=1000,
                     circle=[0, 0, 1], circle_num_points=1000,
                     curve=(lambda x: -x*x, (-1, 1)), curve_num_points=1000, plot=True):

    for cred, num_points in [(poly, poly_num_points), (circle, circle_num_points), (curve, curve_num_points)]:
        res, points, fig = tm.run_test([alg], cred, num_points)
        hull, time_elapsed = res[0]
        print(f"\n\n{'CORRECTNESS_VISUAL: ' + alg.__name__ : >10}")
        print(f"Points: {len(points)}\nHull: {len(hull)}")
        print(f"Time elapsed: {time_elapsed : .2f}s")
        if plot:
            if (hull[0] != hull[-1]):
                hull.append(hull[0])
            pm.plot(points, hull)


def run(algs=_algs):
    for alg in algs:
        test_alg_default(alg)
