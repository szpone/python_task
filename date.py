#!/usr/bin/env/python

from calendar import isleap
from datetime import date
import sys
import itertools as it

THIRTY_DAYS_MONTHS = {4, 6, 9, 11}


def parse_input(input):
    return [int(x) for x in input.split("/")]

def validate_date(year, month, day):

    if isleap(year):
        if month == 2 and day in range(1, 30):
            return date(year, month, day)
    elif not isleap(year) and month == 2 and day in range(1, 29):
        return date(year, month, day)
    else:
        if month in THIRTY_DAYS_MONTHS and day in range(1, 31):
            return dates(year, month, day)
        elif month not in THIRTY_DAYS_MONTHS and month in range(1, 13) and day in range(1, 32):
            return date(year, month, day)

def get_date(num_list):
    permutations = it.permutations(num_list)
    dates_list = []

    for year, month, day in permutations:
        if year in range(2000, 3000):
            if validate_date(year, month, day) is not None:
                dates_list.append(validate_date(year, month, day))

        elif year in range(1000):
            year = 2000 + year
            if validate_date(year, month, day) is not None:
                dates_list.append(validate_date(year, month, day))

    return min(dates_list, default=None)


def main():
    filename = sys.argv[1]

    with open(filename, "r") as f:
        input = f.read().strip()

    date = get_date(parse_input(input))

    if date:
        print(date)
    else:
        print(f"{input} is illegal")



if __name__ == "__main__":
    main()