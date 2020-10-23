from . import test_manager as tm
import pandas as pd
import uuid


def format_output(cred, num, hull, it, times):
    def format_float(t):
        if isinstance(t, float):
            t = f"{t: .4f}"
        return f"{t: >8}"

    return f"{str(cred)[:70]: <75} {str(num): <8} {str(hull): <8} {f'{it}#': >3} " + ' '.join([format_float(t) for t in times])


def run(algs, creds, num_points, filename="Res", iterations=1, view=False, timeout=None):
    writer = pd.ExcelWriter(f"{filename}.xlsx", engine='openpyxl')

    if view:
        for cred in creds:
            tm.view_cred(cred)

    i = 1
    end = len(creds) * len(num_points) * iterations

    for ic, cred in enumerate(creds):
        excel = dict()
        excel['id'] = ['creds', 'n', 'h', 'it'] + \
            [alg.__name__ for alg in algs]
        for num in num_points:
            for it in range(1, iterations+1):
                res, points, fig = tm.run_test(algs, cred, num, timeout)
                hulls = [len(hull) for hull, _ in res]
                hull = sum(hulls) / len(hulls)
                times = [time for _, time in res]
                print(f"({i: >4}/{end})# " +
                      format_output(cred, num, hull, it, times))
                i += 1
                excel[str(uuid.uuid4().hex)] = [cred, num, hull, it] + times

            pd.DataFrame(excel).transpose().to_excel(
                writer, sheet_name=f"Sheet{ic + 1}")
            try:
                writer.save()
            except Exception as e:
                print(e)

    while(True):
        try:
            writer.save()
            break
        except Exception as e:
            print(e, '\n')
    writer.close()
