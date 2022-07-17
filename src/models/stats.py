from re import I
from models.captured import CapturedCollection , CapturedN
from typing import Iterable

class Stats:

    def __init__(self , count : int) -> None:

        self._data: CapturedCollection = CapturedCollection()
        self._count : int = count
    
    def __repr__(self) -> str:
        return f"Stats(stats={[repr(self._data)]}, count={self._count})"
    
    def keys(self) -> Iterable[int]:
        return self._data.keys()
    
    def greater(self, number: int) -> int:
        return self._data[number].greater

    def less(self, number: int) -> int:
        return self._data[number].less

    @property
    def count(self)-> int:
        return self._count

    @property
    def data(self)-> CapturedCollection:
        return self._data


class DataCapture:
    def __init__(self):
        self.count: int = 0
        self.data: CapturedCollection = CapturedCollection()

    def add(self, number: int) -> None:

        if number not in self.data.keys():
            self.data[number] = CapturedN(number)
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