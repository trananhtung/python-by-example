"""Main module."""
from stock.market import Market


def main():
    """Main function."""

    print("Loading data...")
    market = Market('HSX', 'data/CafeF.HSX.Upto24.08.2023.csv')

    while True:
        print("-----------------------------------")
        print('Welcome to Stock Analysis App')
        print('1. Get all stock codes')
        print('2. View chart for a stock')
        print('3. Find up trend stocks')
        print('4. Exit')

        choice = input('Enter your choice: ')
        print("-----------------------------------")
        match choice:
            case '1':
                print(market.get_all_stock_codes())
            case '2':
                code = input('Enter stock code: ')
                try:
                    stock = market.get_stock_instance(code)
                    stock.plot()
                except ValueError:
                    print("Invalid stock code!")
            case '3':
                short_window = int(input('Enter short window: '))
                long_window = int(input('Enter long window: '))
                up_trend_stocks = market.get_up_trend_stocks(
                    short_window, long_window
                )
                print(up_trend_stocks)
            case '4':
                print('Goodbye!')
                break
            case _:
                print('Invalid choice! Please try again.')


if __name__ == '__main__':
    main()
