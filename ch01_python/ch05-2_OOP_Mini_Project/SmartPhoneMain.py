import SmartPhone as sp
import Address as addr

class SmartPhoneMain():
    def printMenu(self):
        print("\n 주소 관리 메뉴")
        print("-" * 20)
        print("1. 연락처 등록")
        print("2. 모든 연락처 출력")
        print("3. 연락처 검색")
        print("4. 연락처 삭제")
        print("5. 연락처 수정")
        print("6. 프로그램 종료")
        print("-" * 20)

    def printMenu_2(self):
        print("\n Contact Manager")
        print("-" * 20)
        print("1. 연락처 등록(회사)")
        print("2. 연락처 등록(거래처)")
        print("3. 모든 연락처 출력")
        print("4. 연락처 검색")
        print("5. 연락처 삭제")
        print("6. 연락처 수정")
        print("7. 프로그램 종료")
        print("-" * 20)

    def Start(self):
        smartphone = sp.SmartPhone()
        addr_data = addr.Addr("홍길동", "010-1234-5678", "santacoding@naver.com", "서울 종로3가", "친구", "1990-01-01")
        smartphone.addAddr(addr_data)
        addr_data = addr.Addr("김선민", "010-1534-4956", "momcoding@naver.com", "서울 관악구", "친구", "2001-03-04")
        smartphone.addAddr(addr_data)

        while True:
            self.printMenu()
            num = int(input("원하는 작업을 선택하세요 (1~6): "))

            if num == 1:            
                smartphone.addAddr(smartphone.inputAddrData())
            elif num == 2:
                smartphone.printAllAddr()
            elif num == 3:
                search_name = input("검색할 연락처의 이름을 입력해주세요: ")
                smartphone.searchAddr(search_name)
            elif num == 4:
                del_name = input("삭제할 연락처의 이름을 입력해주세요: ")
                smartphone.deleteAddr(del_name)
            elif num == 5:
                edit_name = input("수정할 연락처의 이름을 입력해주세요: ")
                smartphone.editAddr(edit_name)
            elif num == 6:
                exit()
            else:
                print("잘못된 번호입니다.")

    def Start_2(self):
        smartphone = sp.SmartPhone()
        addr_data = addr.CompanyAddr("홍길동", "010-1234-5678", "santacoding@naver.com", "서울 종로3가", "네이버", "1990-01-01", "부장", "개발팀")
        smartphone.addAddr(addr_data)
        addr_data = addr.CompanyAddr("김선민", "010-1111-2222", "momcoding@naver.com", "서울 관악구", "삼성 전자", "2001-03-04", "대리", "반도체")
        smartphone.addAddr(addr_data)

        while True:
            self.printMenu_2()
            num = int(input("원하는 작업을 선택하세요 (1~7): "))

            if num == 1:            
                smartphone.addAddr(smartphone.inputCompanyAddrData())
            elif num == 2:
                smartphone.addAddr(smartphone.inputCustomerAddrData())
            elif num == 3:
                smartphone.printAllAddr()
            elif num == 4:
                search_name = input("검색할 연락처의 이름을 입력해주세요: ")
                smartphone.searchAddr(search_name)
            elif num == 5:
                del_name = input("삭제할 연락처의 이름을 입력해주세요: ")
                smartphone.deleteAddr(del_name)
            elif num == 6:
                edit_name = input("수정할 연락처의 이름을 입력해주세요: ")
                smartphone.editAddr(edit_name)
            elif num == 7:
                exit()
            else:
                print("잘못된 번호입니다.")    


if __name__ == "__main__":
    start = SmartPhoneMain()
    #start.Start()
    start.Start_2()