from 파이썬.ch06_Data_Structure_Project.Linked_List import Linked_List

if __name__ == "__main__":
    int_list = Linked_List()
    print("(1) 공백 리스트에 노드 3개 삽입하기")
    int_list.append(1, 3, 7)
    int_list.show_node()
    print("(2) 3노드 뒤에 5노드 삽입하기")
    int_list.insert(5, 2)
    int_list.show_node()
    print("(3) 리스트의 노드를 역순으로 바꾸기")
    int_list.reverse()
    int_list.show_node()
    print("(4) 리스트의 마지막 노드 삭제하기")
    int_list.pop()
    int_list.show_node()

    while True:
        print("1.노드 추가  2.마지막 노드 삭제  3.원하는 위치에 노드 삽입  4.역순으로 바꾸기  5.리스트 출력  6.종료")
        num = int(input("숫자를 입력해주세요: "))
        if num == 1:
            user_input = input("추가할 노드들을 띄어쓰기로 구분하여 입력해주세요: ")
            data_list = list(map(int, user_input.split()))
            int_list.append(*data_list)
        elif num == 2:
            int_list.pop()
        elif num == 3:
            data = int(input("추가 할 노드를 입력해주세요: "))
            position = int(input("원하는 위치를 입력해주세요: "))
            int_list.insert(data, position)
        elif num == 4:
            int_list.reverse()
        elif num == 5:
            int_list.show_node()
        elif num == 6:
            exit()
        else:
            print("잘못된 입력입니다.")
