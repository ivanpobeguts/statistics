import argparse
import os

__author__ = 'Ivan Pobeguts'


def read_operations_file(path):
    with open(path, 'r') as file:
        return file.read().splitlines()


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--sd',
        help='sums by dates file',
        type=str,
    )
    parser.add_argument(
        '--so',
        help='sums by offices file',
        default=0,
        type=int,
    )
    parser.add_argument(
        '--op',
        help='operations file',
        type=str,
    )
    args = check_args(parser)
    return args


def check_args(parser):
    args = parser.parse_args()
    if not os.path.isfile(args.op):
        parser.error(
            "File with offices doesn't exist"
        )
    if os.path.isfile(args.sd):
        parser.error(
            'File with sums by dates already exist'
        )
    if os.path.isfile(args.so):
        parser.error(
            'File with sums by offices already exist'
        )
    return args


if __name__ == '__main__':
    # args = get_args()
    lines = read_operations_file('operations.txt')
    dict = {}
    list = lines[1].split(',')[0]
    # dict[list[2]] = list[3]
    print(list[0])
