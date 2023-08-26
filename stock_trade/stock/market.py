"""Market class for storing stock data."""
from collections import defaultdict

from .stock import Stock
from .utils import load_stock_data


class Market:
    """Market class for storing stock data."""

    def __init__(self, name: str, file_path: str) -> None:
        self.name = name
        self.stocks = self.create_stocks(file_path)

    def create_stocks(self, file_path: str) -> dict[str, Stock]:
        """Create stocks from csv file"""
        csv_file = load_stock_data(file_path)
        stocks_ = defaultdict[str, Stock](None)
        for code, data in csv_file.items():
            stocks_[code] = Stock(code, data)

        return stocks_

    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return f'{self.name} market'

    def get_all_stock_codes(self) -> list:
        """Return all stock codes."""
        return list(self.stocks.keys())

    def get_stock_instance(self, code: str) -> Stock:
        """Create stock instance."""
        if code not in self.stocks:
            raise ValueError(f'{code} does not exist in {self.name} market')
        return self.stocks[code]

    def get_up_trend_stocks(
        self, short_window: int = 50, long_window: int = 200
    ) -> list:
        """Return list of stocks that are in up trend."""
        return [
            stock
            for stock in self.stocks.values()
            if stock.detect_up_trend(short_window, long_window)
        ]
