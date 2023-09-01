"""Test Stock class."""

import unittest

from stock.stock import Stock


class TestStock(unittest.TestCase):
    """Test Stock class."""

    def setUp(self):
        """Set up."""
        self.stock = Stock(
            "AAPL",
            [
                {
                    "date": "2023-08-01",
                    "open": 148.5,
                    "high": 150.2,
                    "low": 147.8,
                    "close": 149.7,
                    "volume": 100000,
                },
                {
                    "date": "2023-08-02",
                    "open": 150.0,
                    "high": 151.5,
                    "low": 149.8,
                    "close": 150.5,
                    "volume": 120000,
                },
            ],
        )

    def test_str(self):
        """Test __str__ function."""
        self.assertEqual(str(self.stock), "AAPL")

    def test_repr(self):
        """Test __repr__ function."""
        self.assertEqual(repr(self.stock), "AAPL")

    def test_detect_up_trend(self):
        """Test detect_up_trend function."""
        result = self.stock.detect_up_trend()
        self.assertTrue(result)

    def test_detect_down_trend(self):
        """Test detect_down_trend function."""
        result = self.stock.detect_down_trend()
        self.assertFalse(result)

    def test_plot(self):
        """Test plot function."""
        self.stock.plot()
