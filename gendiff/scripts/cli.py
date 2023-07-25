import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Compares two configuration files and show a difference.")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help="set format of output")
    args = parser.parse_args()
    print(args)
    return args