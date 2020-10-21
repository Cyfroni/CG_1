from operator import attrgetter


def compare_hulls(h1, h2):
    h1s = sorted(h1, key=attrgetter("x", "y"))
    h2s = sorted(h2, key=attrgetter("x", "y"))
    return h1s == h2s


def assert_sameness(hulls, model=None):
    model = model if model else hulls[0]
    for hull in hulls:
        assert compare_hulls(model, hull)
