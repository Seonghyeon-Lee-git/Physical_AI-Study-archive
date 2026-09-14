# 원소의 값 저장
# 저장할 원소의 형태에 따라 다른 필드로 구성
class Node():
    def __init__(self, node) -> None:
        self.node = node
        self.next = None
        self.data_type = type(node)

    # 타입 검사해서 다음 노드랑 다르면 연결 안되게
    def set_next(self, next_node) -> bool:
        if next_node == None:
            self.next = None
            return True

        if self.data_type != next_node.data_type:
            print(f"{self.data_type.__name__} 노드 뒤에 {next_node.data_type.__name__} 노드를 연결할 수 없습니다!")
            return False

        self.next = next_node
        return True


if __name__ == "__main__":
    print("Linked_List_Main.py에서 실행 해주세요!")