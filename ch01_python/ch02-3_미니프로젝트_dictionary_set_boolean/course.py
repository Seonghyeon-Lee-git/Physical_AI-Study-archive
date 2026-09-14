#STEP1 명단 정리하기(중복 제거)
python_list = ['김민준', '이서연', '박도윤', '이서연', '최지우']
web_list = ['이서연', '박도윤', '한지민', '한지민']

python_set = set(python_list)
web_set = set(web_list)

print(f'파이썬 신청 {len(python_list)}건 -> 실제 {len(python_set)}명')
print(f'파이썬 신청 {len(web_list)}건 -> 실제 {len(web_set)}명')

sorted(python_set)
sorted(web_set)

print(python_set)
print(web_set)


#STEP2 집합 연산으로 명단 비교하기
both = python_set & web_set
all_student = python_set | web_set
only_py = python_set - web_set
only_web = web_set - python_set
one_only = python_set ^ web_set

print(f'둘 다 수강: {both}')
print(f'전체 수강생: {all_student}')
print(f'파이썬만: {only_py}')
print(f'웹개발만: {only_web}')
print(f'한과목만: {one_only}')


#STEP3 불리언으로 판정하기
name = '이서연'
both_bool = bool(name in python_set and web_set)
one_bool = bool(name in python_set or web_set)
no_bool = bool(name not in all_student )
empty = not bool(both)
print(f'이서연 파이썬 수강? {name in python_set}')
print(f'이서연 웹개발 수강? {name in web_set}')
print(f'이서연 둘다 수강? {both_bool}')
print(f'이서연 하나라도 수강? {one_bool}')
print(f'이서연 미수강? {no_bool}')
print(f'교집합이 비었나? {empty}')


#STEP4 딕셔너리로 정리하고 리포트 출력하기
report = {
    'python': len(python_set),
    'web': len(web_set),
    'both': len(both),
    'total':len(all_student)
}
dcr = report['both'] / report['total'] * 100
python = report['python']
web = report['web']
both = report['both']
total = report['total']

print(report)
print("=" * 32)
print(f'{"수 강 현 황":^30}')
print("=" * 32)
print(f'{"파이썬":<14} {python:>10}명')
print(f'{"웹개발":<14} {web:>10}명')
print("-" * 32)
print(f'{"둘 다 수강":<14} {both:>10}명')
print(f'{"전체 인원":<14} {total:>10}명')
print("=" * 32)
print(f'중복 수강률: {dcr:.1f}%')