'''Common utilities for stock analysis.'''

import csv
from collections import defaultdict


def load_stock_data(file_path: str) -> dict:
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
                    'date': date,
                    'open': open_,
                    'high': high,
                    'low': low,
                    'close': close,
                    'volume': volume,
                }
            )

    return stock_data
