from graham_scan import INC_CH
from gift_wrapping import GIFT_CH
from chan_algorithm import CH_CH
from marriage_before_conquest import MbC_CH
import test_manager
import data_manager
from pandas import DataFrame

algs = [INC_CH, GIFT_CH, CH_CH, MbC_CH]


def run(creds, num_points, name="Res"):
    excel = dict()
    excel['name'] = ['creds', 'num', 'hulls'] + [alg.__name__ for alg in algs]

    for cred in creds:
        for num in num_points:
            points, _ = test_manager.gen_points(cred, num)
            times = [test_manager.test_alg(alg, points) for alg in algs]
            hulls = [len(hull) for hull, time in times]
            times = [time for hull, time in times]
            print(f"{cred} /// {num} /// {hulls}", times)
            excel[f"{cred} /// {num}"] = [cred, num, hulls] + times

    DataFrame(excel).transpose().to_excel(
        name + '.xlsx', sheet_name='Sheet1', index=False)


if __name__ == "__main__":
    creds = [
        [(0, 0), (0, 1), (1, 1), (1, 0)],
        [0, 0, 1],
        (lambda x: x*x, (-1, 1))
    ]
    num_points = [10, 100, 1000]

    run(creds, num_points, "1")
