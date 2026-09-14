from 파이썬.ch06_Data_Structure_Project.Node import Node


# 다음 노드의 주소 저장
# append insert pop reverse
class Linked_List():
    def __init__(self) -> None:
        self.node_head = None
        self.node_tail = None

    def append(self, *args) -> None:
        if not args:
            print("추가할 데이터가 없습니다.")
            return

        for node in args:
            new_node = Node(node)

            if self.node_head == None:
                self.node_head = new_node
                self.node_tail = new_node
            else:
                if self.node_tail.set_next(new_node):
                    self.node_tail = new_node
                else:
                    return
        return
    
    def get_length(self) -> int:
        node_len = 0
        curr = self.node_head
        while curr != None:
            node_len += 1
            curr = curr.next
        return node_len

    def find(self, point : int) -> Node:
        if point < 0 or point >= self.get_length():
            return None

        curr = self.node_head
        for i in range(point):
            curr = curr.next

        return curr

    def insert(self, node, point : int) -> None:
        new_node = Node(node)

        if point < 0 or point > self.get_length():
            print(f"잘못된 위치입니다. (0 ~ {self.get_length()})안에서 입력해주세요.")
            return 
        
        if self.node_head == None or point == self.get_length():
            self.append(node)
            return 

        if point == 0:
            if new_node.set_next(self.node_head):
                self.node_head = new_node
                return 
            return 

        prev_node = self.find(point - 1)
        next_node = prev_node.next

        if not new_node.set_next(next_node):
            return 

        if not prev_node.set_next(new_node):
            new_node.next = None 
            return 
        
        return 
        
    def pop(self):
        if self.node_head == None:
            print("리스트가 비어있습니다.")
            return False

        if self.node_head == self.node_tail:
            pop_value = self.node_head.node
            self.node_head = None
            self.node_tail = None
            return pop_value

        prev_node = self.find(self.get_length() - 2)
        pop_value = self.node_tail.node
        prev_node.next = None
        self.node_tail = prev_node

        return pop_value
        
    def reverse(self) -> None:
        old_head = self.node_head

        prev = None
        curr = self.node_head

        while curr != None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        self.node_tail = old_head
        self.node_head = prev

    def show_node(self) -> None:
        current_node = self.node_head
        result = []
    
        while current_node != None:
            result.append(str(current_node.node))
            current_node = current_node.next

        print(f"L = ({', '.join(result)})")


if __name__ == "__main__":
    print("Linked_List_Main.py에서 실행 해주세요!")