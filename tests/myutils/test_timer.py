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