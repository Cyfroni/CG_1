import data_manager as dm
import pandas as pd
import common
import threading
import time
import uuid
try:
    import thread
except ImportError:
    import _thread as thread


def test_alg(alg, points, *args):
    hull = []
    time_elapsed = "error"

    try:
        start = time.time()
        hull = alg(points)
        time_elapsed = time.time() - start
    except KeyboardInterrupt:
        raise
    except Exception as e:
        print(e)

    return hull, time_elapsed


def test_alg_timeout(alg, points, timeout):
    hull = []
    time_elapsed = f"{timeout}+"

    timer = threading.Timer(timeout, thread.interrupt_main)
    timer.start()
    try:
        hull, time_elapsed = test_alg(alg, points)
    except KeyboardInterrupt:
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


def format_output(t):
    if isinstance(t, float):
        t = f"{t: .4f}"
    return f"{t: >8}"


def run(creds, num_points, algs, filename="Res", iterations=1, view=False, timeout=None):
    test_fun = test_alg_timeout if timeout else test_alg
    writer = pd.ExcelWriter(f"{filename}.xlsx", engine='openpyxl')

    if view:
        for cred in creds:
            dm.plot(gen_points(cred, 1000)[0])
    for i in range(1, iterations+1):
        excel = dict()
        excel['name'] = ['creds', 'num', 'hulls'] + \
            [alg.__name__ for alg in algs]
        for cred in creds:
            for num in num_points:
                points, _ = gen_points(cred, num)
                res = [test_fun(alg, points, timeout) for alg in algs]
                hulls = [len(hull) for hull, time in res]
                times = [time for hull, time in res]
                print(
                    f"{f'{i}#': <3} {str(cred)[:50]: <50} {str(num): <7} {str(hulls)[:40]: <40}",
                    ' '.join([format_output(t) for t in times])
                )
                excel[f"{cred} /// {num} /// {uuid.uuid4().hex}"] = [cred,
                                                                     num, hulls] + times

        pd.DataFrame(excel).transpose().to_excel(
            writer, sheet_name=f"Iter {i}")
    writer.save()
    writer.close()
