from . import _algs, _creds, _num_points, tm
from .helpers import assert_sameness


_num_points = _num_points[:2]


def run(algs=_algs, creds=_creds, num_points=_num_points):
    print("\n\nCORRECTNESS\n")
    i = 1
    end = len(creds) * len(num_points)
    for cred in creds:
        for num in num_points:
            print(f"({i}/{end}) ")

            res, _, _ = tm.run_test(algs, cred, num)
            hulls = [hull for hull, _ in res]
            assert_sameness(hulls)

            i += 1
    print("\n\nCORRECTNESS: PASSED\n")
