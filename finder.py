from intens import *
from save import *
from datetime import datetime
from multiprocessing import Process


def sear(alpha, i_start, i_end, index):
    red = []
    delta1 = []
    print("Spawned proc #{}".format(index))
    i = i_start
    j = 0
    h = 0.01
    while i <= i_end:
        start = datetime.now()
        while j <= 0.07:
            loc = search_p(alpha, i, 1.821, j, h)
            # x_list = loc[2]
            y_list = loc[3]
            for k in range(len(x_list)):
                # if x_list[k] <= 0:
                #     blue.append(j)
                #     delta1.append(i)
                #     break
                if y_list[k] <= 0:
                    red.append(j)
                    delta1.append(i)
                    break
                # if k == len(x_list) - 1:
                #     gray.append(j)
                #     delta3.append(i)
            j += 0.0008
        print("{} (elapsed {} sec.)".format(i, (datetime.now() - start).seconds))
        i += 0.0002
        j = 0
    matlab_export(delta1, red, "red_p_{}.txt".format(index))


def main(alpha):
    print(f"Starting at {datetime.now().hour}:{datetime.now().minute}...")
    p1 = Process(target=sear, args=(alpha, 0.06, 0.077, 1))
    p2 = Process(target=sear, args=(alpha, 0.076, 0.091, 2))
    p3 = Process(target=sear, args=(alpha, 0.090, 0.101, 3))
    p4 = Process(target=sear, args=(alpha, 0.100, 0.130881, 4))

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    print("P1 finished")
    p2.join()
    print("P2 finished")
    p3.join()
    print("P3 finished")
    p4.join()
    print("P4 finished")

    print(f"Ending at {datetime.now().hour}:{datetime.now().minute}!")
    #sear(alpha, blue, delta_b, 0.06, 0.130881, 1)
    #matlab_export(delta_b, blue, "blue1.txt")


main(0.4)
