import math


def rect(area):
    a = math.sqrt(area)
    return [(0, 0), (0, a), (a, a), (a, 0)]


def circle(area):
    r = math.sqrt(area / math.pi)
    return [0, 0, r]


def xx_c(area):
    b = (1.5*area) ** (1/3)
    return (lambda x: -x*x, (-b, b))


def disc_c(area):
    r_2 = area / (math.pi/8 - math.sin(math.pi/8) * math.cos(math.pi/8))
    a = math.sqrt(r_2) * math.sin(math.pi/8)
    return (lambda x: math.sqrt(r_2 - x*x), (-a, a))
