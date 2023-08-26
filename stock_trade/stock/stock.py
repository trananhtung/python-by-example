"""Stock class for storing stock data."""
import pandas as pd

import plotly.graph_objects as go


class Stock:
    """Stock class for storing stock data."""

    def __init__(self, code: str, data: list) -> None:
        self.code = code
        self.data = sorted(data, key=lambda x: x['date'])

    def __repr__(self) -> str:
        return self.code

    def __str__(self) -> str:
        return self.code

    def detect_up_trend(
        self, short_window: int = 50, long_window: int = 200
    ) -> bool:
        """Detect up trend."""
        short_ma = (
            sum((s["close"] for s in self.data[-short_window:])) / short_window
        )
        long_ma = (
            sum((s["close"] for s in self.data[-long_window:])) / long_window
        )

        return short_ma > long_ma

    def detect_down_trend(
        self, short_window: int = 50, long_window: int = 200
    ) -> bool:
        """Detect down trend."""
        return not self.detect_up_trend(short_window, long_window)

    def plot(self) -> None:
        """Plot stock data."""

        print(f'Plotting {self.code}...')
        # create data frame from stock data
        data_frame = pd.DataFrame(self.data)

        fig = go.Figure(
            data=[
                go.Candlestick(
                    x=data_frame['date'],
                    open=data_frame['open'],
                    high=data_frame['high'],
                    low=data_frame['low'],
                    close=data_frame['close'],
                )
            ]
        )

        print(data_frame)
        fig.show()
