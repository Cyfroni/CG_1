from . import _algs, _creds, _num_points, em

_creds = _creds[2::5] + _creds[-1:]


def run(algs=_algs, creds=_creds, num_points=_num_points):
    em.run(algs, creds, num_points, filename="exp2_area_c",
           iterations=10, timeout=1000)
