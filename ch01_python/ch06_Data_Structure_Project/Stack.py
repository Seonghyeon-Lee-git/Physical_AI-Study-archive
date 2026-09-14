"""
Stack 인터페이스(interface)와 StackNode
"""
from abc import ABC, abstractmethod


class Stack(ABC):
    """Java의 interface Stack에 대응하는 추상 클래스(abstract class)"""

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def push(self, item:str) -> None:
        pass

    @abstractmethod
    def pop(self) -> str:
        pass

    @abstractmethod
    def delete(self) -> None:
        pass

    @abstractmethod
    def peek(self) -> str:
        pass


if __name__ == "__main__":
    print("Array_Stack_Main.py에서 실행 해주세요!")