from shapely.geometry import Polygon, Point
import random
import types


def domain(x_limits, points):
    x_min, x_max = x_limits
    interval = (x_max - x_min) / (points - 1)
    for x in range(points):
        yield x_min + x * interval


def points_on(fun, x_limits, points=100):
    return [Point([x, fun(x)]) for x in domain(x_limits, points)]


def random_points_within(fig, num_points):
    min_x, min_y, max_x, max_y = fig.bounds
    points = []

    while len(points) < num_points:
        random_point = Point(
            [random.uniform(min_x, max_x), random.uniform(min_y, max_y)])
        if (random_point.within(fig)):
            points.append(random_point)

    return points


def create_fig(cred):
    if all(isinstance(x, int) or isinstance(x, float) for x in cred):
        return Point(cred[0], cred[1]).buffer(cred[2])
    elif all(isinstance(x, tuple) for x in cred):
        return Polygon(cred)
    elif isinstance(cred[0], types.LambdaType):
        return Polygon(points_on(*cred))


def gen_points(cred, num_points):
    fig = create_fig(cred)
    points = []
    if fig:
        points = random_points_within(fig, num_points)
    else:
        points = points_on(cred[1], cred[0], num_points)

    return points, fig
