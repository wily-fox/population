from Stohtr import *
import pylab
import matplotlib.pyplot as plt


def main(alpha, delta):
    my_point = make_data(alpha, delta, 0.5, 0.01)
    #plt.plot(my_point[0], my_point[1], 'b:')
    plt.plot(my_point[1], my_point[0], ':')
    # plt.plot(xy1[0], xy1[1], 'ro', xy2[0], xy2[1], 'ro', xy3[0], xy3[1], 'bo', my_point[0], my_point[1], 'b')
    # plt.axis([0, 100000, 0, 90])
    plt.grid(True)
    pylab.show()


if __name__ == "__main__":
    main(0.4, 0.12)
