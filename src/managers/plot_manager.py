import matplotlib.pyplot as plt
from shapely.geometry import Point


def unzip_p(points):
    return [p.x for p in points], [p.y for p in points]


def unzip_fig(fig):
    fig_p = {(round(x, 8), round(y, 8)) for x, y in fig.exterior.coords}
    return [Point(x, y) for x, y in fig_p]


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
