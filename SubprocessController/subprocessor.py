from typing import List

import subprocess
import sys


class Subprocessor:
    def __init__(self, module_path: str, args: List[str], control_phrase: str, shutdown_phrase: str) -> None:
        """
        Starts given module as a separate subprocess

        :param module_path: absolute path to the module
        :param args: arguments for the module
        :param control_phrase: control phrase to verify module
        :param shutdown_phrase: shutdown phrase to gracefully terminate module
        """

        self.control_phrase = control_phrase
        self.shutdown_phrase = shutdown_phrase
        self.process = subprocess.Popen(args=[sys.executable, module_path] + args, stdin=subprocess.PIPE,
                                        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    def process_command(self, command: str) -> str:
        """
        Strips input command, writes a line, flushes it and returns

        :param command:  command to be written
        :return: subprocess output
        """

        if self.process.poll() is not None:
            raise ValueError("Process is closed.")

        if command is None:
            raise ValueError("command must be defined.")

        self.process.stdin.write(command.strip() + '\n')
        self.process.stdin.flush()

        return self.process.stdout.readline()

    def is_control_phrase_correct(self, control_input: str) -> bool:
        """
        Writes a control input into the subprocess and verifies with the control phrase

        :param control_input: string that will be compared to control phrase
        :return: if verified correctly
        """

        if self.process.poll() is not None:
            raise ValueError("Process is closed.")

        if self.control_phrase is None or control_input is None:
            raise ValueError("control_phrase and control_input must be defined.")

        if self.process_command(control_input).strip() == self.control_phrase.strip():
            return True

        return False

    def close(self) -> None:
        """
        Sends shutdown phrase and waits for termination
        """

        if self.process.poll() is not None:
            raise ValueError("Process is closed.")

        self.process_command(self.shutdown_phrase)
        self.process.wait()
