from typing import Iterable



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
        