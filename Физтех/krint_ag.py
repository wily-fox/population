import math
from el_ag import *
import matplotlib.pyplot as plt
from save import *
from intens_ag import *


def make_data(alpha, delta, x0, y0, sig):
    # main_listx = []
    # main_listy = []
    # list_t = []
    h = 0.1
    for i in range(1000):
        n1 = np.random.normal()
        n2 = np.random.normal()
        km1 = h * f(x0, y0, alpha)
        lm1 = h * g(x0, y0, alpha, delta)
        km2 = h * f(x0 + km1 / 2, y0 + lm1 / 2, alpha)
        lm2 = h * g(x0 + km1 / 2, y0 + lm1 / 2, alpha, delta)
        km3 = h * f(x0 + km2 / 2, y0 + lm2 / 2, alpha)
        lm3 = h * g(x0 + km2 / 2, y0 + lm2 / 2, alpha, delta)
        km4 = h * f(x0 + km3, y0 + lm3, alpha)
        lm4 = h * g(x0 + km3, y0 + lm3, alpha, delta)
        # x1 = x0 + (km1 + 2 * km2 + 2 * km3 + km4) / 6 + x0 * sig * n1 * math.sqrt(h)
        # y1 = y0 + (lm1 + 2 * lm2 + 2 * lm3 + lm4) / 6 - y0 * sig * n2 * math.sqrt(h)
        x1 = x0 + (km1 + 2 * km2 + 2 * km3 + km4) / 6
        y1 = y0 + (lm1 + 2 * lm2 + 2 * lm3 + lm4) / 6 - y0 * y0 * sig * n2 * math.sqrt(h)
        if x1 < 0:
            x1 = 0
        if y1 < 0:
            y1 = 0
        # main_listx.append(x1)
        # main_listy.append(y1)
        # list_t.append(i)
        x0 = x1
        y0 = y1
    return x0


def search_sigma(alpha):
    main_sig = []
    main_del = []
    delta = 0.196565
    h = 0.01
    k = 1.821
    while delta <= 0.22:
        breakme = False
        sig = 0
        while sig <= 0.1:
            # x_ell, y_ell = ellips(alpha, delta, sig, 0.99)
            brbr = search_p(alpha, delta, k, sig, h)
            x_ell = brbr[2]
            y_ell = brbr[3]
            for i in range(len(x_ell)):
                x = x_ell[i]
                y = y_ell[i]
                x1 = make_data(alpha, delta, x, y, sig)
                if x1 > 20:
                    breakme = True
                    main_sig.append(sig)
                    main_del.append(delta)
                    break
            if breakme:
                break
            sig += 0.001
        delta += 0.001
        print(delta)
    return main_sig, main_del


def main(alpha):
    sigma, delta = search_sigma(alpha)
    matlab_export(delta, sigma, "krint_pol_del.txt")
    plt.plot(delta, sigma)
    plt.grid(True)
    pylab.show()


if __name__ == '__main__':
    main(0.4)
