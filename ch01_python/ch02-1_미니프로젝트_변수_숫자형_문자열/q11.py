name = input("이름을 입력하세요: ")
birth = int(input("태어난 해를 입력하세요: "))
age = 2026 - birth

print(type(name), type(birth))
print(f'{name}님은 올해 {age}살입니다.')
print(f'{name}님은 내년이면 {age + 1}살이 됩니다.')