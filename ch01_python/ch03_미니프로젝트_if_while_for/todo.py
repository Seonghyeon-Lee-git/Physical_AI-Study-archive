"""
1. 할 일 추가
2. 할 일 삭제
3. 목록 보기
4. 검색하기
5. 종료
"""

todos = []
todos_num = 0

while True:
    print("1. 할 일 추가")
    print("2. 할 일 삭제")
    print("3. 목록 보기")
    print("4. 검색하기")
    print("5. 종료")

    num = int(input("번호를 선택하세요: "))

    if num == 1:
        todo = input("할 일을 입력해주세요: ")
        todos.append(todo)

        print(f"'{todo}' 추가했습니다. (현재 {len(todos)}개)")
    elif num == 2:
        if len(todos) > 0:
            for i, todo in enumerate(todos,1):
                print(f'{i}. {todo}')

            todo_del_num = int(input("삭제할 번호: "))

            if 1 <= todo_del_num <= len(todos):
                todo_del = todos.pop(todo_del_num - 1)

                print(f"'{todo_del}' 삭제했습니다. (남은 {len(todos)}개)")
            else:
                print("없는 번호입니다.")
        else:
            print("삭제할 할 일이 없습니다.")
    elif num == 3:
        if len(todos) == 0:
            print("등록된 할 일이 없습니다.")
        else:
            print("=" * 30)
            print(f'{"할 일 목록":^30}')
            print("=" * 30)

            for i, todo in enumerate(todos,1):
                print(f'{i}. {todo}')

            print("-" * 30)
            print(f'총 {len(todos)}개')
            print("=" * 30)
    elif num == 4:
        word = input("검색할 단어: ")
        found = [t for t in todos if word in t]

        print(f"'{word}'검색 결과: {len(found)}개")
        for i, todo in enumerate(found,1):
            print(f'{i}. {todo}')
    elif num == 5:
        break
    else:
        print("1~5 중에서 골라 주세요")
