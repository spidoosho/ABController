from argparse import ArgumentParser
import random
import sys

import constants


class Generator:
    def __init__(self, min_value: int, max_value: int) -> None:
        """
        Generates random integers from min_value to max_value

        :param min_value: min possible value
        :param max_value: max possible value
        """

        if not isinstance(min_value, int) or not isinstance(max_value, int):
            raise ValueError("min_value and max_value must be integers")

        self.min = min_value
        self.max = max_value

    def start_cycle(self) -> None:
        """
        Starts input reading cycle
        """

        self.__process_command_cycle()

    def __get_random_integer(self) -> int:
        """
        Gets random integer
        :return: integer between min and max
        """

        return random.randint(self.min, self.max)

    def __process_command(self, command: str) -> bool:
        """
        Based on a command prints a specific message

        :param command: command to be processed
        :return: if reading cycle should continue
        """

        if command == constants.SHUTDOWN_COMMAND_CONST:
            print(constants.SHUTDOWN_OUTPUT_CONST)
            return False

        if command == constants.RANDOM_NUMBER_COMMAND_CONST:
            print(str(self.__get_random_integer()))
        elif command == constants.GREETING_COMMAND_CONST:
            print(constants.GREETING_OUTPUT_CONST)
        else:
            print(constants.ERROR_OUTPUT_CONST)

        return True

    def __process_command_cycle(self) -> None:
        """
        Reads user input and processes it
        """

        continue_cycle = True
        while continue_cycle:
            continue_cycle = self.__process_command(sys.stdin.readline().strip())


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("--min", dest="random_min", required=True, type=int,
                        help="Lowest random number that can be obtained.")
    parser.add_argument("--max", dest="random_max", required=True, type=int,
                        help="Largest random number that can be obtained.")
    args = parser.parse_args()

    gen = Generator(args.random_min, args.random_max)
    gen.start_cycle()
