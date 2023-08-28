"""Fetch rates from API using multithreading."""
import threading

import requests

SYMBOLS = ("USD", "EUR", "PLN", "NOK", "JPY", "CHF", "GBP", "CAD", "AUD")
BASES = ("USD", "EUR", "PLN", "NOK", "JPY", "CHF", "GBP", "CAD", "AUD")


def fetch_rates(base):
    """Fetch rates from API for given base currency."""
    response = requests.get(f"https://api.vatcomply.com/rates?base={base}", timeout=10)
    response.raise_for_status()
    rates = response.json()["rates"]
    rates[base] = 1
    rates_line = ", ".join([f"{rates[symbol]:7.3f} {symbol}" for symbol in SYMBOLS])
    print(f"1 {base} = {rates_line}")


def main():
    """Main function."""
    threads = []
    for base in BASES:
        thread = threading.Thread(target=fetch_rates, args=(base,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
