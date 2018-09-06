from datetime import datetime
import random

__author__ = 'Ivan Pobeguts'


def generate_date():
    current_date = datetime.now()
    current_year = current_date.year
    start_date = datetime(current_year - 1, 1, 1)
    end_date = datetime(current_year, 1, 1)
    random_date = start_date + (end_date - start_date) * random.random()
    print(random_date.strftime("%d.%m.%Y %H:%M"))


if __name__ == '__main__':
    generate_date()
