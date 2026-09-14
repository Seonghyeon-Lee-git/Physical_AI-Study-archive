#STEP1 딕셔너리 만들고 값 꺼내기
student = {
    'name': '김민준',
    'age': 20,
    'major': '컴퓨터공학'
}

print(student)
print(student['name'], student['age'], student['major'])
print(f'학생 수: {len(student)}개 항목')


#STEP2 항목 추가 수정 삭제하기
student['email'] = 'minjun@example.com'
student['hobbies'] = ['python', 'game']
del student['major']
student['age'] = 21

print(student)
print(f'항목 수: {len(student)}')


#STEP3 안전하게 조회하기
print(student.get('name'))
print(student.get('phone'))
print(student.get('phone', '등록되지 않음'))
print('email' in student, 'major' in student)


#STEP4 Key Value 쌍 모아보기
print(list(student.keys()))
print(list(student.values()))
print(list(student.items()))


#STEP5 프로필 카드 출력하기
name = student['name']
age = student['age']
email = student['email']
phone = student.get('phone', '미등록')
hobbies = str(student['hobbies'])
num = len(student)

print("=" * 34)
print(f'{"P R O F I L E":^30}')
print("=" * 34)
print(f'{"이름":<12} {name:<18}')
print(f'{"나이":<12} {age:<18}')
print(f'{"이메일":<12} {email:<18}')
print(f'{"전화":<12} {phone:<18}')
print("-" * 34)
print(f'{"취미":<12} {hobbies:<18}')
print(f'{"이름":<12} {num:<18}')
print("=" * 34)