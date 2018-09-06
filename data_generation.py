from datetime import datetime
import random
import os

__author__ = 'Ivan Pobeguts'


def load_marketplaces(filepath):
    if os.path.isfile(filepath):
        with open(filepath, 'r') as file:
            return file.read().splitlines()
    else:
        return []


def generate_date():
    current_date = datetime.now()
    current_year = current_date.year
    start_date = datetime(current_year - 1, 1, 1)
    end_date = datetime(current_year, 1, 1)
    random_date = start_date + (end_date - start_date) * random.random()
    return random_date.strftime('%d.%m.%Y %H:%M')


def choose_marketplace(filepath):
    marketplaces_list = load_marketplaces(filepath)
    return random.choice(marketplaces_list)


def generate_operation_sum():
    return round(random.uniform(10000.00, 100000.00), 2)


if __name__ == '__main__':
    print(choose_marketplace('marketplaces.txt'))
