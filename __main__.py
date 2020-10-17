from graham_scan import INC_CH
from gift_wrapping import GIFT_CH
from chan_algorithm import CH_CH
from marriage_before_conquest import MbC_CH
import test_manager
import data_manager
import common
import pandas as pd
import time


def format_output(t):
    if isinstance(t, float):
        t = f"{t: .4f}"
    return f"{t: >8}"


def run(creds, num_points, algs, filename="Res", iterations=1, view=False, timeout=None):
    test_fun = test_manager.test_alg_timeout if timeout else test_manager.test_alg
    writer = pd.ExcelWriter(f"{filename}.xlsx", engine='openpyxl')

    if view:
        for cred in creds:
            data_manager.plot(test_manager.gen_points(cred, 1000)[0])
    for i in range(1, iterations+1):
        excel = dict()
        excel['name'] = ['creds', 'num', 'hulls'] + \
            [alg.__name__ for alg in algs]
        for cred in creds:
            for num in num_points:
                points, _ = test_manager.gen_points(cred, num)
                res = [test_fun(alg, points, timeout) for alg in algs]
                hulls = [len(hull) for hull, time in res]
                times = [time for hull, time in res]
                print(
                    f"{f'{i}#': <3} {f'{cred} /// {num} /// {hulls}': <75}",
                    ' '.join([format_output(t) for t in times])
                )
                excel[f"{cred} /// {num}"] = [cred, num, hulls] + times

        pd.DataFrame(excel).transpose().to_excel(
            writer, sheet_name=f"Iter {i}")
    writer.save()
    writer.close()


if __name__ == "__main__":
    creds = [
        [(0, 0), (0, 1), (1, 1), (1, 0)],
        [(0, 0), (0, 5), (5, 5), (5, 0)],
        [0, 0, 1],
        [0, 0, 5],
        # (lambda x: -x*x, (-1, 1))
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

    run(creds, num_points, algs, filename="Res1", iterations=10, timeout=200)
