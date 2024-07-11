from __future__ import annotations
import time
from pathlib import Path

from myutils import timer


def test_Timer():
    timer_ = timer.Timer()

    timer_.start()
    timer_.lap
    timer_.lap
    timer_.stop()
    timer_.reset()

    timer_.lap
    timer_.stop()
    timer_.start()
    timer_.start()
    timer_.reset()
    timer_.lap
    timer_.stop()


def test_TimerWriter():
    timer_ = timer.Timer()

    timer_writer = timer.TimerWriter()
    timer_.start()
    time.sleep(0.01)
    timer_.lap()
    time.sleep(0.01)
    timer_.lap()
    timer_.stop()

    timer_writer(Path("./log.txt", ), timer_)

    timer_.reset()
    timer_writer(Path("./log2.txt"), timer_)


def test_TimerComputer_compute():
    timer_ = timer.Timer()

    for i in range(10):
        timer_.start()
        for j in range(4):
            time.sleep(0.02)
            timer_.lap()
        timer_.stop()


    time_computer = timer.TimerComputer()
    computed = time_computer.compute(timer_.get_datum())

    import csv
    save_file = Path("./out.csv")
    with save_file.open("w") as f:
        writer = csv.writer(f)
        writer.writerows(computed)


def test_TimerComputer_compute_from_csv():
    timer_ = timer.Timer()

    for i in range(10):
        timer_.start()
        for j in range(4):
            time.sleep(0.02)
            timer_.lap()
        timer_.stop()


    writer = timer.TimerWriter()
    time_csv_path = Path("./time.csv")
    writer(time_csv_path, timer_)

    time_computer = timer.TimerComputer()
    computed = time_computer.compute_from_csv(time_csv_path)

    import csv
    save_file = Path("./out.csv")
    with save_file.open("w") as f:
        writer = csv.writer(f)
        writer.writerows(computed)