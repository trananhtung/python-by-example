"""Test utils module."""

import unittest
from collections import defaultdict
from unittest.mock import mock_open, patch

from stock.utils import convert_date_from_yyyymmdd_to_yyyy_mm_dd, load_stock_data


class TestLoadStockData(unittest.TestCase):
    """Test load_stock_data function."""

    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data="code,date,open,high,low,close,volume\nAAPL,20230801,148.5,150.2,147.8,149.7,100000\nAAPL,20230802,150.0,151.5,149.8,150.5,120000\n",
    )
    def test_load_stock_data(self, mock_file):
        """Test load_stock_data function."""
        expected_data = defaultdict(list)
        expected_data["AAPL"].append(
            {
                "date": "2023-08-01",
                "open": 148.5,
                "high": 150.2,
                "low": 147.8,
                "close": 149.7,
                "volume": 100000,
            }
        )
        expected_data["AAPL"].append(
            {
                "date": "2023-08-02",
                "open": 150.0,
                "high": 151.5,
                "low": 149.8,
                "close": 150.5,
                "volume": 120000,
            }
        )

        result = load_stock_data("dummy_path")

        self.assertAlmostEqual(result, expected_data)
        self.assertEqual(mock_file.call_count, 1)
        self.assertEqual(mock_file.call_args[0][0], "dummy_path")


class TestConvertDate(unittest.TestCase):
    """Test convert_date_from_yyyymmdd_to_yyyy_mm_dd function."""

    def test_convert_date(self):
        """Test convert_date_from_yyyymmdd_to_yyyy_mm_dd function."""
        result = convert_date_from_yyyymmdd_to_yyyy_mm_dd("20230801")
        self.assertEqual(result, "2023-08-01")

    def test_convert_date_with_invalid_date(self):
        """Test convert_date_from_yyyymmdd_to_yyyy_mm_dd function."""
        with self.assertRaises(ValueError):
            convert_date_from_yyyymmdd_to_yyyy_mm_dd("2023080")

    def test_convert_date_with_invalid_date_format(self):
        """Test convert_date_from_yyyymmdd_to_yyyy_mm_dd function."""
        with self.assertRaises(ValueError):
            convert_date_from_yyyymmdd_to_yyyy_mm_dd("202308011")

    def test_convert_date_with_invalid_date_type(self):
        """Test convert_date_from_yyyymmdd_to_yyyy_mm_dd function."""
        with self.assertRaises(TypeError):
            convert_date_from_yyyymmdd_to_yyyy_mm_dd("qweqweqwe")
