import argparse
import os
import sys

from lib import iter_single_cpp_lines


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--include', nargs='*', default=[])

    args = parser.parse_args()

    args.include.append('.')
    args.include = [os.path.abspath(path) for path in args.include]

    return args


def main():
    args = parse_args()

    for line in iter_single_cpp_lines(
        in_lines=sys.stdin, 
        include_dirs=args.include,
    ):
        print(line)


if __name__ == '__main__':
    main()
