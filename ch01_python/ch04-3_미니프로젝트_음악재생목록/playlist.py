from collections import deque


queue = deque() # 재생 대기열 - 큐(FIFO)
history = []    # 재생 이력 - 스택(LIFO)
now = None      # 현재 재생 중인 곡


# 현재 음악재생 목록을 보여주는 함수
def show_status(now):
    print("=" * 44)
    print(f"{'M Y P L A Y L I S T':^30}")
    print("=" * 44)
    now = now if now is not None else "(없음)"
    print(f"현재 재생 {now:>9}")
    print("-" * 44)
    print(f"대기열 {len(queue):>3}곡 (먼저 넣은 곡부터 재생)")
    if len(queue) == 0:
        print("(비어 있음)")
    else:
        for i, queue_song in enumerate(queue, 1):
            print(f"{i}. {queue_song}")
    print("-" * 44)
    print(f"재생 이력 {len(history):>3}곡 (최근에 들은 곡부터)")
    if len(history) == 0:
        print("(비어 있음)")
    else:
        for i, history_song in enumerate(reversed(history), 1):
            print(f"{i}. {history_song}")
    
    print("=" * 44)


# 입력받은 곡을 queue 맨 뒤에 추가하는 함수
def add_song(title):
    queue.append(title)
    print(f"'{title}'을(를) 대기열 맨 뒤에 추가했습니다. (총 {len(queue)}곡)")


# queue의 제일 앞을 리턴하는 함수
def play_next(now):
    if len(queue) == 0: 
        print("대기열이 비어있습니다.")
        return now
    else:
        next = queue.popleft()
        print(f"재생: {next}")
        if now is not None:
            history.append(now)
        return next


# 리스트의 제일 마지막을 리턴하는 함수
def play_prev(now):
    if len(history) == 0:
        print("재생 이력이 비어있습니다.")
        return now
    else:
        if now is not None:
            queue.appendleft(now)
        prev = history.pop()
        print(f"이전 곡 재생: {prev}")
        return prev
        

# 입력받은 곡을 queue 제일 앞에 추가하는 함수
def add_urgent(title):
    queue.appendleft(title)
    print(f"'{title}'을(를) 대기열 맨 앞에 넣었습니다. (총 {len(queue)}곡)")


# queue를 입력받은 n만큼 회전하는 함수
def rotate_queue(n):
    queue.rotate(n)
    print(f"대기열을 {n}칸 회전했습니다.")
    print(f"{list(queue)}")

"""
1.곡 추가 2.다음 곡 3.이전 곡 
4.맨 앞에 넣기 5.대기열 회전 6.현재 상태 0.종료
"""

while True:
    print("1.곡 추가 2.다음 곡 3.이전 곡 \n 4.맨 앞에 넣기 5.대기열 회전 6.현재 상태 0.종료")

    num = int(input("번호를 선택하세요: "))

    if num == 1:
        title = input("추가할 곡 제목: ")
        add_song(title)
    elif num == 2:
        now = play_next(now)
    elif num == 3:
        now = play_prev(now)
    elif num == 4:
        urgent = input("추가할 곡 제목: ")
        add_urgent(urgent)
    elif num == 5:
        rotate = int(input("회전할 칸 수를 입력해주세요: "))
        rotate_queue(rotate)
    elif num == 6:
        show_status(now)
    elif num == 0:
        print("종료하겠습니다.")
        exit()
    else:
        print("없는 번호입니다.")