from operator import attrgetter


def compare_hulls(h1, h2):

    # print(h1)
    # print(h2)

    h1 = sorted(h1, key=attrgetter("x", "y"))
    h2 = sorted(h2, key=attrgetter("x", "y"))

    # for i in range(len(h1)):
    #     print(h1[i], h2[i])

    return h1 == h2


def assert_sameness(hulls, model=None):

    # print(hulls)

    model = model if model else hulls[0]
    for hull in hulls:
        assert compare_hulls(model, hull)
