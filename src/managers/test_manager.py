from . import plot_manager as pm
from . import data_manager as dm
import time
import threading
import _thread


def run_alg(alg, points, *args):
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


def run_alg_timeout(alg, points, timeout):
    hull = []
    time_elapsed = f"{timeout}+"

    timer = threading.Timer(timeout, _thread.interrupt_main)
    timer.start()
    try:
        hull, time_elapsed = run_alg(alg, points)
    except KeyboardInterrupt:
        pass
    finally:
        timer.cancel()

    return hull, time_elapsed


def view_cred(cred):
    pm.plot(dm.gen_points(cred, 10000)[0])


def run_test(algs, cred, num_points, timeout=None):
    run_fun = run_alg_timeout if timeout else run_alg
    points, fig = dm.gen_points(cred, num_points)
    res = [run_fun(alg, points, timeout) for alg in algs]
    return res, points, fig
