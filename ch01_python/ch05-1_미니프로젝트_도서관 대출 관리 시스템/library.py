from abc import ABC, abstractmethod


class LibraryItem(ABC):
    total_items = 0

    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
        self.is_loaned = False
        self.borrower = None
        LibraryItem.total_items += 1

    @abstractmethod
    def loan_period(self):
        pass

    @abstractmethod
    def info(self):
        pass

    def checkout(self, name):
        if self.is_loaned == True:
            print(f"'{self.title}'은(는) 이미 {self.borrower}님이 대출 중입니다.")
            return False
        else:
            print(f"{name}님, '{self.title}' 대출 완료! (대출 기간 {self.loan_period()}일)")
            self.is_loaned = True
            self.borrower = name
            return True

    def return_item(self):
        if self.is_loaned == False:
            print("대출 중이 아닙니다.")
            return False
        else:
            print(f"{self.borrower}님이 '{self.title}'을(를) 반납했습니다.")
            self.is_loaned = False
            self.borrower = None
            return True


class Book(LibraryItem):
    def __init__(self, title, item_id, author, pages):
        super().__init__(title, item_id)
        self.author = author
        self.pages = pages

    def loan_period(self):
        return 14

    def info(self):
        return f"[도서] {self.title} / {self.author} / {self.pages}쪽"

class DVD(LibraryItem):
    def __init__(self, title, item_id, director, minutes):
        super().__init__(title, item_id)
        self.director = director
        self.minutes = minutes

    def loan_period(self):
        return 7

    def info(self):
        return f"[DVD] {self.title} / {self.director} 감독 / {self.minutes}분"


class Magazine(LibraryItem):
    def __init__(self, title, item_id, issue):
        super().__init__(title, item_id)
        self.issue = issue

    def loan_period(self):
        return 3

    def info(self):
        return f"[잡지] {self.title} / {self.issue}호"


class Library():
    def __init__(self, name):
        self.name = name
        self.items = []

    def add(self, item):
        self.items.append(item)
        print(f"'{item.title}' 등록완료 (총 {len(self.items)}개)")

    def find(self, item_id):
        for item in self.items:
            if item_id == item.item_id:
                return item
        return None

    def show_all(self):
        print("=" * 56)
        print(f"{self.name:^30}")
        print("=" * 56)
        print(f"{'ID':<6} {'정보':<32} {'상태':>14}")
        print("-" * 56)
        for item in self.items:
            state = f"대출중({item.borrower})" if item.is_loaned else "대출가능"
            print(f"{item.item_id:<6} {item.info():<32} {state:>5}")
        print("=" * 56)

    def report(self):
        reports = {}
        for item in self.items:
            reports[type(item).__name__] = reports.get(type(item).__name__, 0) + 1
            
        sorted(reports, key = lambda x : reports[x], reverse = True)
        loan_num = len([i for i in self.items if i.is_loaned])

        print("-" * 56)
        print(f"{'종류별 등록 현황':^30}")
        print("-" * 56)
        for report in reports:
            print(f"{report:<6} {reports[report]:>13}개")
        print("-" * 56)
        print(f"{'대출 중':<6} {loan_num:>13}개")
        print(f"{'전체 등록':<6} {LibraryItem.total_items:>13}개 (클래스변수)")
        print("-" * 56)


lib = Library("한 빛 도 서 관")
lib.add(Book("파이썬 입문", "B001", "박응용", 480))
lib.add(Book("자료구조", "B002", "김철수", 320))
lib.add(DVD("인터스텔라", "D001", "놀란", 169))
lib.add(Magazine("과학동아", "M001", 9))

"""
1. 전체 목록    2. 통계    3. 대출    4. 반납   0.종료
"""
while True:
    print("\n 1. 전체 목록    2. 통계    3. 대출    4. 반납   0.종료")
    num = int(input("번호를 선택하세요: "))
    if num == 1:
        lib.show_all()
    elif num == 2:
        lib.report()
    elif num == 3:
        id = input("대출할 자료 번호: ").upper()
        if lib.find(id) == None:
            print("없는 번호입니다.")
            continue
        else:
            name = input("대출자 이름: ")
            lib.find(id).checkout(name)
    elif num == 4:
        id = input("반납할 자료 번호: ").upper()
        if lib.find(id) == None:
            print("없는 번호입니다.")
            continue
        else:
            lib.find(id).return_item()
    elif num == 0:
        exit()
    else:
        print("없는 번호입니다.")