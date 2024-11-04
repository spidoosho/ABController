from typing import List
from SubprocessController import Subprocessor
from statistics import median
import os


def get_random_integers_array(process: Subprocessor, count: int) -> List[int]:
    """
    Retrieves random integers based on given count
    :param process: process from which random numbers will be obtained
    :param count: number of desired random integers
    :return: List of integers of given count
    """

    arr = []
    for i in range(count):
        value = process.process_command("GetRandom")
        arr.append(int(value))
    return arr


if __name__ == '__main__':
    count = 100
    min_val = 1
    max_val = 100

    module_path = os.path.abspath(r".\NumberGenerator\generator.py")
    args = ["--min", str(min_val), "--max", str(max_val)]

    generator = Subprocessor(module_path, args, "Hi", "Shutdown")
    generator.process_command("GetRandom")

    number_arr = get_random_integers_array(generator, count)
    number_arr.sort()

    print(f"Average of {count} random integers is {sum(number_arr) / len(number_arr)}")
    print(f"Median of {count} random integers is {median(number_arr)}")
