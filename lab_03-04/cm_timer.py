import time
from contextlib import contextmanager
from time import sleep


class cm_timer_1:
    def __init__(self):
        self.startTime = 0

    def __enter__(self):
        self.startTime = time.time()
        return self

    def __exit__(self, a, b, c):
        endTime = time.time() - self.startTime
        print(f"cm_timer_1: Time {endTime}s")


@contextmanager
def cm_timer_2():
    nowTime = time.time()
    try:
        yield
    finally:
        print(f'cm_timer_2: Time {time.time() - nowTime}s')


def test():
    with cm_timer_1():
        sleep(2.3)

    with cm_timer_2():
        sleep(2.2)

# test()
