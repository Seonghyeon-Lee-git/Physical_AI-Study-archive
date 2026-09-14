import sys


FILE = "records.txt"
CATEGORIES = {"식비", "교통", "문화", "기타"}


# 파일에 기록을 추가하는 함수
def add_record(date, category, item, amount):
    with open(FILE, 'a', encoding = "utf-8") as file:
        file.write(f"{date},{category},{item},{amount}\n")

    print(f"기록했습니다. ({date}, {category}, {item}, {amount:,}원)")


# 기록된 파일을 읽어서 딕셔너리로 저장하고 리스트로 반환
def load_records():
    records = []

    with open(FILE, 'a', encoding = "utf-8") as file:
        pass

    with open(FILE, 'r', encoding = "utf-8") as file:
        for line in file:
            line = line.strip()
            date, category, item, amount = line.split(",")
            record = {
                "date": date, 
                "category": category, 
                "item": item, 
                "amount": int(amount),
                }
            records.append(record)

    return records


# 파일에 기록된 정보를 보여주는 함수
def show_all():
    records = load_records()

    if len(records) == 0:
        print("아직 기록이 없습니다.")
        return 0
    else:
        print("=" * 46)
        print(f"{'용 돈 기 록 장':^30}")
        print("=" * 46)
        print(f"{'번호':<5} {'날짜':<7} {'분류':<7} {'내용':<7} {'금액':>7}")
        print("-" * 46)
        for i, record in enumerate(records,1):
            print(f"{i:<5} {record['date']:<7} {record['category']:<7} {record['item']:<9} {record['amount']:>9,}")
        print("-" * 46)
        print(f"합계 {sum(record['amount'] for record in records):^30}")
        print("=" * 46)


# 파일에 기록된 정보를 분류별로 통계 내는 함수
def summary():
    records = load_records()
    if len(records) == 0:
        print("아직 기록이 없습니다.")
    else:
        by_category = {
            "총 지출": 0,
            "문화": 0,
            "식비": 0,
            "교통": 0,
        }
        for record in records:
            by_category["총 지출"] += record['amount']
            c = record['category']
            if c in by_category:
                by_category[c] += record['amount']
            else:
                by_category[c] = record['amount']

        sorted(by_category, key = lambda k: by_category[k], reverse = True)

        print("-" * 46)
        print(f"{'분류별 지출':^30}")
        print("-" * 46)
        for category in by_category:
            if category == "총 지출":
                continue
            if by_category["총 지출"] != 0:
                amount_percent = by_category[category] / by_category["총 지출"] * 100
            print(f"{category:<5} {by_category[category]:>11,} {amount_percent:>13.1f}%")
        print("-" * 46)
        print(f"{'총 지출':<5} {by_category['총 지출']:>11,}원")
        print(f"{'기록 수':<5} {len(records):>11}건")
        print(f"{'평균':<5} {int(by_category['총 지출']/len(records)):>11,}원")
        print("-" * 46)


# 파일에 기록된 정보에서 내용이나 분류를 검색하는 함수
def search(word):
    records = load_records()
    found = [r for r in records if word in r["item"] or word in r["category"]]
    print(f"'{word}' 검색 결과: {len(found)}건")
    for i, record in enumerate(found,1):
        print(f"{i}. {record['date']} {record['category']} {record['item']} {record['amount']:,}원")
    if len(found) > 0:
        print(f"합계 {sum(record['amount'] for record in found)}원")


args = sys.argv[1:]
if len(args) > 0:
    if args[0] == "list":
        show_all()
    elif args[0] == "sum":
        summary()
    elif args[0] == "find" and len(args) > 1:
        search(args[1])
    else:
        print("사용법: python money.py [list / sum / find 검색어]")
else:
    while True:
        print("1.기록추가 2.전체 보기 3.통계 4.검색 0.종료")
        num = int(input("번호를 선택하세요: "))

        if num == 1:
            date = input("날짜(예: 2026-08-24): ")
            print(f"분류: {CATEGORIES}")
            category = input("분류: ")
            if category not in CATEGORIES:
                print("카테고리에 없는 내용입니다.")
                continue
            item = input("내용: ")
            amount = int(input("금액: "))
            add_record(date, category, item, amount)
        elif num == 2:
            show_all()
        elif num == 3:
            summary()
        elif num == 4:
            word = input("검색하실 단어를 입력해주세요: ")
            search(word)
        elif num == 0:
            print("감사합니다.")
            exit()
        else:
            print("없는 번호입니다.")
