import pylab
import matplotlib.pyplot as plt


def f(alpha, delta, x, y):
    return x - x*y/(1+alpha*x) - 0.01*x*x


def g(alpha, delta, x, y):
    return -y + x*y/(1+alpha*x) - delta*y*y


def search(alpha, delta, x, y):
    node_x = []
    node_y = []
    dx, dy = (x, y)
    h = 0.01
    for i in range(1000):
        km1 = h*f(alpha, delta, dx, dy)
        lm1 = h*g(alpha, delta, dx, dy)
        km2 = h*f(alpha, delta, dx + km1/2, dy + lm1/2)
        lm2 = h*g(alpha, delta, dx + km1/2, dy + lm1/2)
        km3 = h*f(alpha, delta, dx + km2/2, dy + lm2/2)
        lm3 = h*g(alpha, delta, dx + km2/2, dy + lm2/2)
        km4 = h*f(alpha, delta, dx + km3, dy + lm3)
        lm4 = h*g(alpha, delta, dx + km3, dy + lm3)
        x1 = dx + (km1 + 2*km2 + 2*km3 + km4)/6
        y1 = dy + (lm1 + 2*lm2 + 2*lm3 + lm4)/6
        node_x.append(x1)
        node_y.append(y1)
        dx = x1
        dy = y1

    return node_x, node_y


x0, y0 = search(0.4, 0.2, 12, 6)
plt.plot(x0, y0)
plt.grid(True)
pylab.show()
