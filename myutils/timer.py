from __future__ import annotations
import time
from pathlib import Path


class Timer:
    def __init__(self):
        self._starting_time: float = time.time()
        self._is_started: bool = False
        self._elapsed_times: list[float] = []
        self._elapsed_times_list: list[list[float]] = []
        self._last_time:float = 0.0


    def _print_is_started(self):
        print("Error: Timer is already start ! Should 'stop'")


    def _print_is_not_started(self):
        print("Error: Timer is not start ! Should 'start'")


    def start(self):
        if self._is_started:
            self._print_is_started()
            return
        self._last_time = self._starting_time = time.time()
        self._is_started = True


    def lap(self):
        if not self._is_started:
            self._print_is_not_started()
            return
        now_time = time.time()
        elapsed_time: float = now_time - self._last_time
        self._last_time = now_time
        self._elapsed_times.append(elapsed_time)


    def stop(self):
        if not self._is_started:
            self._print_is_not_started()
            return
        self.lap()
        elapsed_time: float = time.time() - self._starting_time
        self._elapsed_times.append(elapsed_time)

        self._elapsed_times_list.append(self._elapsed_times)
        self._elapsed_times = []
        self._is_started = False


    def reset(self):
        if self._is_started:
            self._print_is_started()
            return
        self._is_started = False
        self._elapsed_times_list.clear()


    def get_datum(self) -> list[list[float]]:
        return self._elapsed_times_list


class TimerWriter:
    def __call__(self, save_file:Path, timer:Timer):
        assert save_file.parent.exists(), f"Not Found Save dir is '{save_file.parent}'"

        datum: list[list[float]] = timer.get_datum()
        if self._is_not_zero(datum): return

        texts :list[str] = [self._create_titles(datum)]
        texts += self._convert_texts(datum)

        # save
        text: str = "\n".join(texts)
        with save_file.open("w") as f:
            f.write(text)


    def _is_not_zero(self, datum:list[list[float]]):
        if len(datum) == 0:
            print("timer data is zero, so do not save")
            return True
        else:
            return False


    def _create_titles(self, datum:list[list[float]]) -> str :
        num_data: int = len(datum[0])
        titles: list[str] = [f"lap{ni:>05}" for ni in range(1, num_data)]
        titles.append("all")
        title: str = ", ".join(titles)
        return title


    def _convert_texts(self, datum:list[list[float]]) -> list[str]:
        texts: list[str] = []
        for data in datum:
            words: list[str] = [f"{di:>.8f}" for di in data]
            text: str = ", ".join(words)
            texts.append(text)
        return texts