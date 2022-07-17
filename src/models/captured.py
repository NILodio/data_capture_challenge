from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable

@dataclass()
class CapturedNumber:
    def __init__(self, value: int):
        self.value: int = value
        self.less: int = 0
        self.greater: int = 0
        self.count: int = 0

    def __str__(self):
        return str(
            {
                "value": self.value,
                "less": self.less,
                "greater": self.greater,
                "count": self.count,
            }
        )

    def __repr__(self):
        return f"CapturedNumber(value={self.value}, less={self.less}, greater={self.greater}, count={self.count})"


@dataclass()
class CapturedCollection:
    def __init__(self) -> None:
        self.collection: dict[int, CapturedNumber] = {}
        self.current_iteration: int = 0

    def __iter__(self) -> CapturedCollection:
        return self

    def __next__(self) -> CapturedNumber:
        while self.current_iteration < 999:
            self.current_iteration += 1
            if self.current_iteration not in self.collection:
                return CapturedNumber(self.current_iteration)
            else:
                return self.collection[self.current_iteration]

        self.current_iteration = 0
        raise StopIteration

    def __repr__(self) -> str:
        return repr(self.collection)

    def __setitem__(self, key: int, value: CapturedNumber) -> None:
        if key < 1 or key > 999:
            raise ValueError("Error {}".format(number=key))
        self.collection[key] = value

    def __getitem__(self, key: int) -> CapturedNumber:
        if key < 1 or key > 999:
            raise ValueError("Error {}".format(number=key))
        if key not in self.collection:
            self.collection[key] = CapturedNumber(key)
        return self.collection[key]

    def keys(self) -> Iterable[int]:
        return self.collection.keys()