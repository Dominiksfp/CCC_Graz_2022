import os
from pprint import pprint

import level1
import level2
import level3
import level4
import level5
import level6
import level7
from classes import *


def load(input_data):
    n = int(input_data[0])

    return Data(n=n)


if __name__ == "__main__":
    level, quests = 1, 5
    for q in range(0, quests + 1):
        if q == 0:
            q = "example"

        input_file = r'/home/thomas/Downloads/level{0}/level{0}_{1}.in'.format(level, q)
        output_file = os.path.splitext(input_file)[0] + ".out"

        with open(input_file, 'r') as fi:
            data = load(fi.read().splitlines())
            pprint(data)

            print("=== Input {}".format(q))
            print("======================")

            if level == 1:
                result = level1.solve(data)
            elif level == 2:
                result = level2.solve(data)
            elif level == 3:
                result = level3.solve(data)
            elif level == 4:
                result = level4.solve(data)
            elif level == 5:
                result = level5.solve(data)
            elif level == 6:
                result = level6.solve(data)
            elif level == 7:
                result = level7.solve(data)

            pprint(result)

            with open(output_file, 'w+') as fo:
                fo.write(result)
