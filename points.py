import random
import matplotlib.pyplot as plt
from shapely.geometry import Polygon, Point

def domain(x_limits, num_points):
    x_min, x_max = x_limits
    interval = (x_max - x_min) / num_points
    for x in range(num_points):
        yield x_min + x * interval

def random_points_within(fig, num_points):
    min_x, min_y, max_x, max_y = fig.bounds
    points = []
    
    while len(points) < num_points:
        random_point = Point([random.uniform(min_x, max_x), random.uniform(min_y, max_y)])
        if (random_point.within(fig)):
            points.append(random_point)

    return points

def points_on(fun, x_limits, num_points):
    return [Point([x, fun(x)]) for x in domain(x_limits, num_points)]

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

def plot(points, hull=None, fig=None):
    plot_p(points)
    if hull:
        plot_hull(hull)
    if fig:
        plot_fig(fig)

    plt.show()

def create_circle(x, y, r):
    return Point(x, y).buffer(r)

def create_poly(points):
    return Polygon(points)

def test(alg, 
        poly=[(0, 0), (0, 1), (1, 1), (1, 0)], poly_num_points=1000,
        circle=[0, 0, 1], circle_num_points=1000,
        curve=lambda x: x*x, curve_limits=(-1, 1), curve_num_points=1000, 
        plot_fig=False):

    fig = create_poly(poly)
    points = random_points_within(fig, poly_num_points)
    hull = alg(points)
    plot(points, hull, fig if plot_fig else None)

    fig = create_circle(*circle)
    points = random_points_within(fig, circle_num_points)
    hull = alg(points)
    plot(points, hull, fig if plot_fig else None)

    points = points_on(curve, curve_limits, curve_num_points)
    hull = alg(points)
    plot(points, hull)


if __name__ == "__main__":
    test(lambda x: [], plot_fig=True)