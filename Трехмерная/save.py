import os


def matlab_export(x_list, y_list, filename="export.txt"):
    # if os.path.isfile(filename):
        # raise FileExistsError("This file already exists!")
    with open(filename, mode="w") as file:
        for line in map(lambda x, y: "{} {}".format(x, y), x_list, y_list):
            file.write("{}\n".format(line))


def matlab_export_1(x_list, filename="export.txt"):
    # if os.path.isfile(filename):
        # raise FileExistsError("This file already exists!")
    with open(filename, mode="w") as file:
        for line in map(lambda x: "{}".format(x), x_list):
            file.write("{}\n".format(line))
