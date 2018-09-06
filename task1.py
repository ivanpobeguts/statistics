from datetime import datetime
import random
import os
import argparse
import time
from multiprocessing import Pool
from functools import partial

__author__ = 'Ivan Pobeguts'


def load_offices(filepath):
    with open(filepath, 'r') as file:
        return file.read().splitlines()


def generate_date():
    current_date = datetime.now()
    current_year = current_date.year
    start_date = datetime(current_year - 1, 1, 1)
    end_date = datetime(current_year, 1, 1)
    random_date = start_date + (end_date - start_date) * random.random()
    return random_date


def choose_office(path):
    offices_list = load_offices(path)
    return random.choice(offices_list)


def generate_operation_sum():
    return round(random.uniform(10000.00, 100000.00), 2)


def prepare_result_string(path, num):
    prep_string = [
        str(num + 1),
        generate_date().date().strftime('%d.%m.%Y'),
        generate_date().time().strftime('%H:%M'),
        choose_office(path),
        str(generate_operation_sum()),
    ]
    result_string = ','.join(prep_string)
    return result_string


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--of',
        help='path to offices file',
        type=str,
    )
    parser.add_argument(
        '--num',
        help='number of operations',
        default=0,
        type=int,
    )
    parser.add_argument(
        '--op',
        help='path to output file',
        default='operations.txt',
        type=str,
    )
    args = check_args(parser)
    return args


def check_args(parser):
    args = parser.parse_args()
    if args.of is None:
        parser.error(
            "Please specify file with offices"
        )
    if not os.path.isfile(args.of):
        parser.error(
            "File with offices doesn't exist"
        )
    if args.num == 0:
        parser.error(
            'You must enter non zero number of operations'
        )
    if args.op is None:
        parser.error(
            "Please specify output file with operations"
        )
    return args


if __name__ == '__main__':
    before = int(round(time.time() * 1000))
    args = get_args()
    p = Pool(5)
    with open(args.op, 'w') as f:
        prep_header = [
            'Num',
            'Date',
            'Time',
            'Office_num',
            'Ammount',
        ]
        header = ','.join(prep_header)
        f.write('%s\n' % header)
        for result in p.map(
                partial(prepare_result_string, args.of),
                range(args.num)):
            f.write('%s\n' % result)

    after = int(round(time.time() * 1000))
    print('File successfully saved! Time spent: {} ms'
          .format(after - before))
