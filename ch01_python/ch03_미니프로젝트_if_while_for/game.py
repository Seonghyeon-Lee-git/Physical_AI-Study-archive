
answer = 37
count = 0
history = []

while count < 5:
    count += 1
    num = int(input(f"[{count}/5] 숫자를 입력하세요(1~100): "))
    history.append(num)
    if num > answer:
        print("DOWN! 더 작은 수를 입력하세요.")
    elif num < answer:
        print("UP! 더 큰 수를 입력하세요.")
    else:
        print(f"정답입니다! {count}번 만에 맞혔습니다.")
        break

result = "성공" if num == answer else "실패"
too_big = [g for g in history if g > answer]
too_small = [g for g in history if g < answer]
too_big_num = len(too_big)
too_small_num = len(too_small)

print("=" * 34)
print(f'{"게 임 결 과":^38}')
print("=" * 34)
print(f'{"정답":<14} {answer:>18}')
print(f'{"시도 횟수":<14} {count:>18}')
print(f'{"결과":<14} {result:>18}')
print("-" * 34)
print(f'{"입력 기록":<14} {history}')
print(f'{"너무 큰 수":<14} {too_big_num:>18}')
print(f'{"너무 작은 수":<14} {too_small_num:>18}')
print("=" * 34)