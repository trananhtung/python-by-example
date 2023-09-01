import time
from queue import Empty, Queue
from threading import Thread

import requests


SYMBOLS = ("USD", "EUR", "PLN", "NOK", "CZK")
BASES = ("USD", "EUR", "PLN", "NOK", "CZK")

THREADS = 4


def fetch_rates(base):
    """Fetch rates from API for given base currency."""
    response = requests.get(f"https://api.vatcomply.com/rates?base={base}", timeout=10)
    response.raise_for_status()
    rates = response.json()["rates"]
    # note: same currency exchanges to itself 1:1
    rates[base] = 1.0
    return base, rates


def present_result(base, rates):
    """Present result of fetching rates from API."""
    rates_line = ", ".join([f"{rates[symbol]:10.03} {symbol}" for symbol in SYMBOLS])
    print(f"1 {base} = {rates_line}")


def worker(work_queue: Queue, results_queue):
    """Worker thread."""
    while not work_queue.empty():
        try:
            item = work_queue.get_nowait()
        except Empty:
            break
        else:
            base, rates = fetch_rates(item)
            results_queue.put((base, rates))
            work_queue.task_done()


def main():
    """Main function."""
    work_queue = Queue()
    results_queue = Queue()
    for base in BASES:
        work_queue.put(base)
    threads = [
        Thread(target=worker, args=(work_queue, results_queue)) for _ in range(THREADS)
    ]
    for thread in threads:
        thread.start()

    work_queue.join()
    while threads:
        threads.pop().join()
    while not results_queue.empty():
        present_result(*results_queue.get())


if __name__ == "__main__":
    started = time.time()
    main()
    elapsed = time.time() - started
    print()
    print("time elapsed: {:.2f}s".format(elapsed))
