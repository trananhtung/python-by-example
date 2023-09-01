"""Demo of throttling."""

from threading import Lock, Thread
from queue import Empty, Queue
import time
import random
import hashlib


class Throttle:
    """Throttle class."""

    def __init__(self, rate):
        """Initialize."""
        self._consume_lock = Lock()
        self.rate = rate
        self.tokens = 0
        self.last = None

    def __repr__(self):
        """Repr."""
        return f"{self.__class__.__name__}(rate={self.rate})"

    def consume(self, amount=1):
        """Consume tokens."""
        with self._consume_lock:
            now = time.time()
            if self.last is None:
                self.last = now
            elapsed = now - self.last
            self.last = now
            self.tokens += elapsed * self.rate
            self.tokens = min(self.tokens, self.rate)
            if self.tokens < amount:
                return False
            self.tokens -= amount
            return True


def create_random_password(length=8):
    """Create random password."""
    password = ""
    while len(password) < length:
        password += random.choice(
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        )
    return password


def hash_password(password):
    """Hash password."""
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def worker_throttled(work_queue: Queue, results_queue: Queue, throttle) -> None:
    """Worker thread."""
    while not work_queue.empty():
        try:
            limit = work_queue.get_nowait()
        except Empty:
            break
        else:
            while not throttle.consume():
                time.sleep(0.5)

            password = create_random_password(limit)
            hashed = hash_password(password)
            results_queue.put((password, hashed))
            break


MAX_THREADS = 10_000
RATE = 100


def main():
    """Show throttling in thread."""
    work_queue = Queue()
    results_queue = Queue()
    for _ in range(MAX_THREADS):
        work_queue.put(random.randint(5, 50))
    threads = [
        Thread(
            target=worker_throttled,
            args=(work_queue, results_queue, Throttle(rate=RATE)),
        )
        for _ in range(MAX_THREADS)
    ]
    for thread in threads:
        thread.start()

    while threads:
        threads.pop().join()
    while not results_queue.empty():
        print(results_queue.get())


if __name__ == "__main__":
    started = time.time()
    main()
    elapsed = time.time() - started
    print(f"Elapsed: {elapsed:.2f}s")
