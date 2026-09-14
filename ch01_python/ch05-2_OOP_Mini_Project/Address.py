class Addr():
    def __init__(self, name, phone_num, email, address, group, birth):
        self.name = name
        self.phone_num = phone_num
        self.email = email
        self.address = address
        self.group = group
        self.birth = birth

    def show_info(self):
        print(f"이름: {self.name}")
        print(f"전화번호: {self.phone_num}")
        print(f"이메일: {self.email}")
        print(f"주소: {self.address}")
        print(f"생일: {self.birth}")


class CompanyAddr(Addr):
    def __init__(self, name, phone_num, email, address, group, birth,  position, department):
        super().__init__(name, phone_num, email, address, group, birth)
        self.department = department
        self.position = position

    def show_info(self):
        super().show_info()
        print(f"직급: {self.position}")
        print(f"회사 이름: {self.group}")
        print(f"부서: {self.department}")



class CustomerAddr(Addr):
    def __init__(self, name, phone_num, email, address, group, birth,  position, item):
        super().__init__(name, phone_num, email, address, group, birth)
        self.item = item
        self.position = position

    def show_info(self):
        super().show_info()
        print(f"직급: {self.position}")
        print(f"거래처 이름: {self.group}")
        print(f"품목 이름: {self.item}")


if __name__ == "__main__":
    print("SmartPhoneMain.py로 실행 해주세요.")