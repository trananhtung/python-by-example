"""Example of using multiprocessing module."""

from multiprocessing import Process
import os


def worker(identifier):
    """Worker."""
    print(f"Worker {identifier} starting, pid: {os.getpid()}")


def main():
    """Start worker processes."""
    processes = []
    for i in range(5):
        process = Process(target=worker, args=(i,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()


if __name__ == "__main__":
    main()
