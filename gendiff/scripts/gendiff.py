#! /usr/bin/env python3
from gendiff.find_diff import find_difference
from gendiff.scripts.cli import parse_args
from gendiff.output_diff import generate_diff


def main():
    args = parse_args()
    diff = find_difference(args.first_file, args.second_file)
    result = generate_diff(diff)
    print(result)


if __name__ == "__main__":
    main()