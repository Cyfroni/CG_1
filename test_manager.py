import data_manager as dm
import time
import threading
try:
    import thread
except ImportError:
    import _thread as thread


def test_alg(alg, points, *args):
    start = time.time()
    hull = alg(points)
    time_elapsed = time.time() - start
    return hull, time_elapsed


def test_alg_timeout(alg, points, timeout):
    hull = []
    time_elapsed = f"{timeout}+"

    timer = threading.Timer(timeout, thread.interrupt_main)
    timer.start()
    try:
        hull, time_elapsed = test_alg(alg, points)
    except:
        pass
    finally:
        timer.cancel()

    return hull, time_elapsed


def gen_points(cred, num_points):
    fig = dm.create_fig(cred)
    points = []
    if fig:
        points = dm.random_points_within(fig, num_points)
    else:
        points = dm.points_on(cred, num_points)

    return points, fig


def _test(alg, cred, num_points):

    points, fig = gen_points(cred, num_points)
    hull, time_elapsed = test_alg(alg, points)

    return points, hull, fig, time_elapsed


def test(alg,
         poly=[(0, 0), (0, 1), (1, 1), (1, 0)], poly_num_points=1000,
         circle=[0, 0, 1], circle_num_points=1000,
         curve=(lambda x: -x*x, (-1, 1)), curve_num_points=1000, plot=True):

    times = []
    for cred, num_points in [(poly, poly_num_points), (circle, circle_num_points), (curve, curve_num_points)]:
        points, hull, fig, time_elapsed = _test(alg, cred, num_points)
        print(f"\n\nPLOT\nPoints: {len(points)}\nHull: {len(hull)}")
        print(f"Time elapsed: {time_elapsed : .2f}s")
        times.append(time_elapsed)
        if plot:
            dm.plot(points, hull)
    return times
