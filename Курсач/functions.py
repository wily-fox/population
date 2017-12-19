def pr_f_x(alpha, x, y):
    return 1 - y/(1 + alpha * x)**2 - 0.02 * x


def pr_f_y(alpha, x):
    return - x / (1 + alpha * x)


def pr_g_x(alpha, x, y):
    return y / (1 + alpha * x) ** 2


def pr_g_y(alpha, delta, x, y):
    return -1 + x / (1 + alpha * x) - 2 * delta * y


def f(x, y, alpha):
    return x - (x * y) / (1 + alpha * x) - 0.01 * x * x


def g(x, y, alpha, delta):
    return - y + (x * y) / (1 + alpha * x) - delta * y * y


def func(alpha, delta, x):
    return -1-alpha*x+x-delta*(1+2*alpha*x+(alpha**2)*x**2-0.01*x-0.02*alpha*x**2-0.01*(alpha**2)*x**3)


def pr_func(alpha, delta, x):
    return -alpha+1-delta*(2*alpha+2*(alpha**2)*x-0.01-0.04*alpha*x-0.03*(alpha**2)*x**2)


def func_y(alpha, delta, x):
    return ((x / (1 + alpha * x)) - 1)/delta
