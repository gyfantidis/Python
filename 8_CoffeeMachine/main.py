from coffees import MENU
from coffees import resources


def insertCoins():
    coins = 0
    coins = coins + (0.25 * int(input("how many quarters?: ")))
    coins = coins + (0.1 * int(input("how many dimes?: ")))
    coins = coins + (0.05 * int(input("how many nickles?: ")))
    coins = coins + (0.21 * int(input("how many pennies?: ")))
    return coins

def monayControlCheck(coffeType, usersCoins, money):
    cost = MENU[coffeType]["cost"]
    change = usersCoins - cost

    if change < 0:
        print("Sorry that's not enough money. Money refunded.")
        return money
    else:
        print(f"Here is ${change} in change.")
        print(f"Here is your {coffeType} ☕️. Enjoy!")
        return money + cost

def checkResources(coffee):
    for item in resources:
        cofRef = MENU[coffee]["ingredients"][item]
        if resources[item] - cofRef < 0:
            print("Sorry there is not enough water.")
            return False
        else:
            return True

def reduceResources(coffee):
    for item in resources:
        resources[item] = resources[item] - MENU[coffee]["ingredients"][item]


def game():
    shouldStop = True
    money = 0;
    while shouldStop:
        coffee = input("What would you like? (espresso/latte/cappuccino): * 'report' for resources report : ")

        if coffee == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${money}")
        else:
            if checkResources(coffee):
                print("please insert coins.")
                money = monayControlCheck(coffee, insertCoins(), money)
                reduceResources(coffee)
            anotherCoffee = input("Do you want another coffee? 'Y for yes, 'N for no: ").lower()
            if anotherCoffee == 'n':
                shouldStop=False



game()




