# Coffee Machine Program
 
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


#주문을 만들 수 있을 때는 True를 반환, 재료가 부족할 경우에는 False 반환
def is_resource_sufficient(order_ingredients):
    for ingredient in order_ingredients:
        if order_ingredients[ingredient] > resources[ingredient]:
            print(f'죄송합니다. {ingredient}가 충분하지 않습니다.')
            return False

    return True
            

#투입된 동전으로 계산된 총액을 반환
def process_coins():
    quarters = int(input("쿼터($0.25) 동전을 갯수를 입력해주세요: "))
    dimes = int(input("다임($0.10) 동전을 갯수를 입력해주세요: "))
    nickels = int(input("니켈($0.05) 동전을 갯수를 입력해주세요: "))
    pennies = int(input("페니($0.01) 동전을 갯수를 입력해주세요: "))

    coins = 0.25 * quarters + 0.1 * dimes + 0.05 * nickels + 0.01 * pennies
    print(f'총 ${coins:.2f}를 받았습니다.')
    return coins


#지불이 승인되면 True를 반환, 금액이 부족하면 False를 반환
def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = money_received - drink_cost
        print(f'거스름돈 ${change:.2f}를 돌려드립니다.')
        return True
    else:
        print("죄송합니다. 금액이 부족합니다. 돈이 환불되었습니다.")

    return False


#자원(resources)에서 필요한 재료(ingredients)를 차감
def make_coffee(drink_name, order_ingredients):
    for ingredient in order_ingredients:
        resources[ingredient] -= order_ingredients[ingredient]

    print(f'여기 {drink_name}가 나왔습니다. 즐기세요!')


# 남은 자원과 수익을 보여주는 함수
def show_report():
    print(f'물: {resources["water"]}')
    print(f'우유: {resources["milk"]}')
    print(f'커피: {resources["coffee"]}')
    print(f'돈: {profit}')


while True:
    order_coffee = input("어떤 음료를 원하시나요? (espresso / latte / cappuccino): ")

    if order_coffee == "off":
        exit()
    elif order_coffee == "report":
        show_report()
    elif order_coffee == "espresso" or order_coffee == "latte" or order_coffee == "cappuccino":
        order_ingredient = MENU[order_coffee]["ingredients"]
        drink_cost = MENU[order_coffee]["cost"]

        if is_resource_sufficient(order_ingredient):
            money_received = process_coins()
            
            if is_transaction_successful(money_received, drink_cost):
                make_coffee(order_coffee, order_ingredient)
                profit += drink_cost
    else:
        print("잘못된 입력입니다. 다시 입력해주세요.")

                

        
         