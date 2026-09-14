from 파이썬.ch06_Data_Structure_Project.Stack import Stack
from 파이썬.ch06_Data_Structure_Project.Node import Node


class Linked_Stack(Stack):
    def __init__(self):
        self.top_node = None

    def is_empty(self) -> bool:
        if self.top_node == None:
            return True
        return False

    def push(self, node) -> None:
        new_node = Node(node)

        if self.is_empty():
            self.top_node = new_node
            return True

        if new_node.set_next(self.top_node):
            self.top_node = new_node
            return True
        else:
            return False

    def pop(self) -> str:
        if self.is_empty():
            print("스택이 비어있습니다.")
            return None

        pop_node = self.top_node.node
        self.top_node = self.top_node.next
        return pop_node

    def delete(self) -> None:
        self.top_node = None

    def peek(self) -> str:
        if self.is_empty():
            print("스택이 비어있습니다.")
            return None

        return self.top_node.node

    def show_stack(self):
        curr = self.top_node
        result = []
        while curr != None:
            result.append(curr.node)
            curr = curr.next
        result.reverse()
        print(f"Array Stack>> {', '.join(result)}")


if __name__ == "__main__":
    print("Array_Stack_Main.py에서 실행 해주세요!")