from datetime import datetime
import random
import os
import argparse

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
    return random_date.strftime('%d.%m.%Y %H:%M')


def choose_office(path):
    offices_list = load_offices(path)
    return random.choice(offices_list)


def generate_operation_sum():
    return round(random.uniform(10000.00, 100000.00), 2)


def write_to_file(path, string):
    with open(path, 'a') as the_file:
        the_file.write(string + '\n')


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
        type=str,
    )
    args = check_args(parser)
    return args


def check_args(parser):
    args = parser.parse_args()
    if not os.path.isfile(args.of):
        parser.error(
            "File with offices doesn't exist"
        )
    if os.path.isfile(args.op):
        parser.error(
            "File with offices already exist"
        )
    if args.num == 0:
        parser.error(
            "You must enter non zero number of operations"
        )
    return args


if __name__ == '__main__':
    args = get_args()
    with open(args.op, 'w') as output_file:
        for num in range(args.num):
            string = str(num + 1), generate_date(), choose_office(args.of), str(generate_operation_sum())
            result_string = ' '.join(string)
            output_file.write("%s\n" % result_string)
