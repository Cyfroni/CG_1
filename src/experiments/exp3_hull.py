from . import _algs2, _creds, _num_points, tm, dm, pm, em
import random
import pandas as pd
import uuid

_cred = _creds[-1]
_num = _num_points[-2]
_hulls_points = _num_points[:-2]
# del _algs[3]


def run(algs=_algs2, hulls_points=_hulls_points):
    writer = pd.ExcelWriter(f"exp3_hull.xlsx", engine='openpyxl')

    excel = dict()
    excel['id'] = ['creds', 'n', 'h', 'it'] + \
        [alg.__name__ for alg in algs]

    iterations = 10
    i = 1
    end = len(_hulls_points) * iterations
    for h in hulls_points:
        for it in range(1, iterations + 1):
            fig_p, _ = dm.gen_points(_cred, h)
            fig_cred = [(p.x, p.y) for p in fig_p]
            points, fig = dm.gen_points(fig_cred, _num-h)
            points += fig_p
            random.shuffle(points)

            res = [tm.run_alg_timeout(alg, points, timeout=1000)
                   for alg in algs]

            hulls = [len(hull) for hull, _ in res]
            hull = sum(hulls) / len(hulls)
            times = [time for _, time in res]
            print(f"({i: >4}/{end})# " +
                  em.format_output(_cred, _num, hull, it, times))
            i += 1
            excel[str(uuid.uuid4().hex)] = [_cred, _num, hull, it] + times

        pd.DataFrame(excel).transpose().to_excel(
            writer, sheet_name=f"Hulls")

    while(True):
        try:
            writer.save()
            break
        except Exception as e:
            print(e, '\n')
    writer.close()
