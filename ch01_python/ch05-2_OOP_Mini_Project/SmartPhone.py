import Address as addr


class SmartPhone():
    def __init__(self):
        self.data = []

    def input_basic_info(self):
        name = input("이름을 입력하세요: ")
        phone_num = input("전화번호를 입력하세요: ")
        email = input("이메일을 입력하세요: ")
        address = input("주소를 입력하세요: ")
        birth = input("생일을 입력하세요(예: 1990-01-01): ")
        
        return name, phone_num, email, address, birth

    def inputAddrData(self):
        name, phone_num, email, address, birth = self.input_basic_info()
        group = input("그룹(친구/가족)을 입력하세요: ")
        
        return addr.Addr(name, phone_num, email, address, group, birth)

    def inputCompanyAddrData(self):
        name, phone_num, email, address, birth = self.input_basic_info()
        position = input("직급을 입력하세요: ")
        group = input("회사 이름을 입력하세요: ")
        department = input("부서를 입력하세요: ")
        
        return addr.CompanyAddr(name, phone_num, email, address, group, birth, position, department)

    def inputCustomerAddrData(self):
        name, phone_num, email, address, birth = self.input_basic_info()
        position = input("직급을 입력하세요: ")
        group = input("거래처 이름을 입력하세요: ")
        item = input("품목 이름을 입력하세요: ")
        
        return addr.CustomerAddr(name, phone_num, email, address, group, birth, position, item)
    
    def addAddr(self, data):
        self.data.append(data)
        print(f"데이터가 저장되었습니다. (현재 {len(self.data)}개)")

    def printAddr(self, data):
        print(f"이름: {data.name}")
        print(f"전화번호: {data.phone_num}")
        print(f"이메일: {data.email}")
        print(f"주소: {data.address}")
        print(f"그룹(친구 / 가족): {data.group}")

    def printAllAddr(self):
        if self.data:
            for i, d in enumerate(self.data, 1):
                print(f"\n[{i}]")
                #self.printAddr(d)
                d.show_info()
        else:
            print("저장된 연락처가 없습니다.")

    def searchAddr(self, name):
        for d in self.data:
            if name == d.name:
                #self.printAddr(d)
                d.show_info()
                return True
        print("저장된 연락처에 존재하지 않는 이름입니다.")
        return False

    def deleteAddr(self, name):
        for i, d in enumerate(self.data, 0):
            if name == d.name:
                print(f"{d.name}님의 연락처가 삭제되었습니다.")
                del self.data[i]
                return True
        print("저장된 연락처에 존재하지 않는 이름입니다.")
        return False

    def editAddr(self, name):
        for i, d in enumerate(self.data, 0):
            if name == d.name:
                if type(d) == addr.CompanyAddr:
                    self.data[i] = self.inputCompanyAddrData()
                elif type(d) == addr.CustomerAddr:
                    self.data[i] = self.inputCustomerAddrData()
                else: 
                    self.data[i] = self.inputAddrData()
                return True
        print("저장된 연락처에 존재하지 않는 이름입니다.")
        return False


if __name__ == "__main__":
    print("SmartPhoneMain.py로 실행 해주세요.")