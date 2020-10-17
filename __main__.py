from graham_scan import INC_CH
from gift_wrapping import GIFT_CH
from chan_algorithm import CH_CH
from marriage_before_conquest import MbC_CH
import test_manager
import data_manager
import common
from pandas import DataFrame
import time

algs = [INC_CH, GIFT_CH, CH_CH, MbC_CH]


def run(creds, num_points, filename="Res", view=False, timeout=None):
    excel = dict()
    excel['name'] = ['creds', 'num', 'hulls'] + [alg.__name__ for alg in algs]

    test_fun = test_manager.test_alg_timeout if timeout else test_manager.test_alg

    if view:
        for cred in creds:
            data_manager.plot(test_manager.gen_points(cred, 1000)[0])

    for cred in creds:
        for num in num_points:
            points, _ = test_manager.gen_points(cred, num)
            res = [test_fun(alg, points, timeout) for alg in algs]
            hulls = [len(hull) for hull, time in res]
            times = [time for hull, time in res]
            print(f"{cred} /// {num} /// {hulls}", times)
            excel[f"{cred} /// {num}"] = [cred, num, hulls] + times

    DataFrame(excel).transpose().to_excel(
        filename + '.xlsx', sheet_name='Sheet1', index=False)


if __name__ == "__main__":
    creds = [
        [(0, 0), (0, 1), (1, 1), (1, 0)],
        [(0, 0), (0, 5), (5, 5), (5, 0)],
        [0, 0, 1],
        [0, 0, 5],
        (lambda x: -x*x, (-1, 1))
    ]
    num_points = [
        100,
        1000,
        10000
    ]

    run(creds, num_points, filename="5", timeout=200)
