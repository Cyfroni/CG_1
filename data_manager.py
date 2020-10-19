import random
import matplotlib.pyplot as plt
from shapely.geometry import Polygon, Point
import types


def domain(x_limits, points):
    x_min, x_max = x_limits
    interval = (x_max - x_min) / (points - 1)
    for x in range(points):
        yield x_min + x * interval


def random_points_within(fig, num_points):
    min_x, min_y, max_x, max_y = fig.bounds
    points = []

    while len(points) < num_points:
        random_point = Point(
            [random.uniform(min_x, max_x), random.uniform(min_y, max_y)])
        if (random_point.within(fig)):
            points.append(random_point)

    return points


def points_on(fun, x_limits, points=100):
    return [Point([x, fun(x)]) for x in domain(x_limits, points)]


def unzip_p(points):
    return [p.x for p in points], [p.y for p in points]


def unzip_fig(fig):
    return fig.exterior.xy


def plot_p(points):
    plt.scatter(*unzip_p(points), s=0.5)


def plot_fig(fig):
    plt.plot(*unzip_fig(fig), color='black', linewidth=1)


def plot_hull(hull):
    plt.plot(*unzip_p(hull), color='red', linewidth=2)


def plot(points, hull=[], fig=None):
    # plt.ylim(5, 17)
    # plt.xlim(-6, 6)
    plot_p(points)
    if hull:
        plot_hull(hull)
    if fig:
        plot_fig(fig)

    plt.show()


def create_fig(cred):
    if all(isinstance(x, int) or isinstance(x, float) for x in cred):
        return Point(cred[0], cred[1]).buffer(cred[2])
    elif all(isinstance(x, tuple) for x in cred):
        return Polygon(cred)
    elif isinstance(cred[0], types.LambdaType):
        return Polygon(points_on(*cred))


def calc_bottom_hull(upper_hull, points):
    inv_p = [Point(-p.x, -p.y) for p in points]
    return [Point(-p.x, -p.y) for p in upper_hull(inv_p)]
