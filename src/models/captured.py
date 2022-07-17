from typing import Iterable
from dataclasses import dataclass

MAX_VALUE = 999

@dataclass()
class CapturedN:
    def __init__(self , value: int) -> None:


        self.value = value
        self.less = 0
        self.greater = 0
        self.count = 0
    

    def __str__(self) -> str:
        ### https://www.educative.io/answers/what-is-the-str-method-in-python
        return str(
            {
                "value" : self.value,
                "less": self.less,
                "greater": self.greater,
                "count": self.count,
            }
        )


    def __repr__(self):
        ### https://www.educative.io/answers/what-is-the-repr-method-in-python
        return f"CapturedN(value={self.value}, less={self.less}, greater={self.greater}, count={self.count})"

@dataclass()
class CapturedCollection:


    def __init__(self) -> None:

        self.collection : dict[int , CapturedN] = {}
        self.iteration = 0
    

    def __repr__(self) -> str:
        return repr(self.collection)


    def keys(self) -> Iterable[int]:
        return self.collection.keys()

    
    def __next__(self) -> CapturedN:
        while self.iteration < MAX_VALUE:
            self.iteration += 1
            if self.iteration not in self.collection:
                return CapturedN(self.iteration)
            else:
                return self.collection[self.iteration]

        self.iteration = 0
        raise StopIteration
    
    def __setitem__(self, key: int, value: CapturedN) -> None:

        if key < 1 or key > MAX_VALUE:
            raise ValueError("number {} is not in range".format(number=key))
        self.collection[key] = value
    
    def __getitem__(self, key: int) -> CapturedN:

        if key < 1 or key > MAX_VALUE:
            raise ValueError("number {} is not in range".format(number=key))
        if key not in self.collection:
            self.collection[key] = CapturedN(key)
        return self.collection[key]
    

