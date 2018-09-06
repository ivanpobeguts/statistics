import argparse
import os
from datetime import datetime

__author__ = 'Ivan Pobeguts'


def read_operations_file(path):
    with open(path, 'r') as file:
        return file.read().splitlines()


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--sd',
        help='sums by dates file',
        default='sums-by-dates.txt',
        type=str,
    )
    parser.add_argument(
        '--so',
        help='sums by offices file',
        default='sums-by-offices.txt',
        type=str,
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
    if args.op is None:
        parser.error(
            "Please specify file with operations"
        )
    if not os.path.isfile(args.op):
        parser.error(
            "File with offices doesn't exist"
        )
    return args


def sum_by_offices(op_info):
    sum_dict = {}
    for i in range(1, len(op_info) - 1):
        op_details_lst = op_info[i].split(',')
        sum_dict[op_details_lst[3]] = round(sum_dict.get(op_details_lst[3], 0) + float(op_details_lst[4]), 2)
    sorted_sum_dict = sorted(
        sum_dict.items(),
        key=lambda x: x[1],
        reverse=True
    )
    return sorted_sum_dict


def sum_by_dates(op_info):
    sum_dict = {}
    for i in range(1, len(op_info) - 1):
        op_detail_lst = op_info[i].split(',')
        sum_dict[op_detail_lst[1]] = round(sum_dict.get(op_detail_lst[1], 0) + float(op_detail_lst[4]), 2)
    sorted_sum_dict = sorted(
        sum_dict.items(),
        key=lambda x: datetime.strptime(x[0], '%d.%m.%Y')
    )
    return sorted_sum_dict


def write_dict_to_file(input_dict, path):
    with open(path, 'w') as f:
        for k, v in input_dict:
            file_string = ':'.join([k, str(v)])
            f.write('%s\n' % file_string)


if __name__ == '__main__':
    args = get_args()
    op_info = read_operations_file(args.op)
    if len(op_info) == 0:
        print('Warning! Your operations file is empty.')
    write_dict_to_file(
        sum_by_offices(op_info),
        args.so
    )
    write_dict_to_file(
        sum_by_dates(op_info),
        args.sd
    )
    print('Files successfully saved!')
