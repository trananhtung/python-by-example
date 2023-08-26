'''Common utilities for stock analysis.'''

import csv
from collections import defaultdict


def load_stock_data(file_path: str) -> dict[str, list]:
    '''Load stock from csv file and return a dict of stock data.'''
    stock_data = defaultdict(list)
    with open(file_path, 'r', newline='', encoding="utf8") as csv_file:
        # remove first line of csv_file
        reader = csv.reader(csv_file)
        # remove header
        next(reader)
        for row in reader:
            [code, date, open_, high, low, close, volume] = row
            stock_data[code].append(
                {
                    'date': convert_date_from_yyyymmdd_to_yyyy_mm_dd(date),
                    'open': float(open_),
                    'high': float(high),
                    'low': float(low),
                    'close': float(close),
                    'volume': int(volume),
                }
            )
    return stock_data


def convert_date_from_yyyymmdd_to_yyyy_mm_dd(date: str) -> str:
    '''Convert date to from YYYYMMDD to YYYY-MM-DD.'''

    if not date.isnumeric():
        raise TypeError('Date must be numeric')

    if len(date) != 8:
        raise ValueError('Date must be in YYYYMMDD format')

    return f'{date[:4]}-{date[4:6]}-{date[6:]}'
