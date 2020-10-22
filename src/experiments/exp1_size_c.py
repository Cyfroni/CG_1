from . import _algs2, _creds, _num_points, em

_num_points = _num_points[-2:-1]
_creds = _creds[:-1]


def run(algs=_algs2, creds=_creds, num_points=_num_points):
    em.run(algs, creds, num_points, filename="exp1_size_c", iterations=10)
