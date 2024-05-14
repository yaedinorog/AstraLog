# This file created for parsing arguments in terminal
# Our program will have few(~6) arguments for easy terminal use

import argparse


def parser_args():
    """
    Function for parsing arguments in terminal.
    Return object with arguments.
    """
    # Create parser for arguments
    parser = argparse.ArgumentParser("Parser Log", description="A program for parsing logs")

    # Path to file
    parser.add_argument("log_file", type=str, help="Path to log file.")
    # Levels for logs
    parser.add_argument("-l", "--level", metavar="", type=str, default="INFO",
                        choices=["ERROR", "DEBUG", "INFO", "WARNING", "warning", "Warning","error"],
                        help="Level logs for searching (choices {).")
    # Time for logs
    parser.add_argument("-t", "--time", metavar="", type=int, default=30,
                        help="Selecting the time from which to show logs. (In minutes)")

    return parser.parse_args()
