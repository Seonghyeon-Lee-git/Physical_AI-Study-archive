from 파이썬.ch06_Data_Structure_Project.Array_Stack import Linked_Stack

if __name__ == "__main__":
    stack = Linked_Stack()
    print("Inserted Item: A")
    stack.push("A")
    stack.show_stack()
    print("Inserted Item: B")
    stack.push("B")
    stack.show_stack()
    print("Inserted Item: C")
    stack.push("C")
    stack.show_stack()
    print("deleted Item: C")
    stack.pop()
    stack.show_stack()

    while True:
        print("1.스택 추가  2.마지막 스택 삭제  3.스택 초기화  4.마지막 스택 확인  5.리스트 출력  6.종료")
        num = int(input("숫자를 입력해주세요: "))
        if num == 1:
            data = input("추가할 스택을 입력 해주세요: ")
            stack.push(data)
        elif num == 2:
            stack.pop()
        elif num == 3:
            stack.delete()
        elif num == 4:
            stack.peek()
        elif num == 5:
            stack.show_stack()
        elif num == 6:
            exit()
        else:
            print("잘못된 입력입니다.")