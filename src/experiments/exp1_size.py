from . import _algs, _creds, _num_points, em

_num_points = _num_points[3:4]


def run(algs=_algs, creds=_creds, num_points=_num_points):
    em.run(algs, creds, num_points, filename="exp1", iterations=10)
