import re
from typing import Iterable

from models.captured import CapturedNumber , CapturedCollection



class Stats:
    def __init__(self, count: int) -> None:
        self._data: CapturedCollection = CapturedCollection()
        self._count: int = count

    def __repr__(self) -> str:
        return f"Stats(stats={[repr(self._data)]}, count={self._count})"

    def __setitem__(self, key: int, item: CapturedNumber) -> None:
        self._data[key] = item

    def __getitem__(self, key: int) -> CapturedNumber:
        return self._data[key]

    @property
    def count(self) -> int:
        return self._count

    @property
    def data(self) -> CapturedCollection:
        return self._data

    def between(self, a: int, b: int) -> int:
        if a < b:
            lowest, highest = a, b
        else:
            lowest, highest = b, a

        return self._count - self._data[lowest].less - self._data[highest].greater

    def greater(self, number: int) -> int:
        return self._data[number].greater

    def keys(self) -> Iterable[int]:
        return self._data.keys()

    def less(self, number: int) -> int:
        return self._data[number].less


class DataCapture:
    def __init__(self):
        self.count: int = 0
        self.data: CapturedCollection = CapturedCollection()

    def add(self, number: int) -> None:
        if number not in self.data.keys():
            self.data[number] = CapturedNumber(number)
        self.data[number].count += 1
        self.count += 1

    def build_stats(self) -> Stats:
        stats: Stats = Stats(self.count)
        less: int = 0
        greater: int = self.count

        for i in self.data:
            stats[i.value].count = i.count
            stats[i.value].less = less
            stats[i.value].greater = greater - i.count
            less += i.count
            greater -= i.count

        return stats