from data import MENU, resources


# TODO Prompt the user by asking what would he like
def ask_user():
    decision = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()
    return decision


# TODO Print report
def print_report(resources, money):
    print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: {money}")


# TODO Check resources sufficient?
def check_resources(resources, option, MENU):
    water = resources["water"] >= MENU[option]["ingredients"]["water"]
    coffee = resources["coffee"] >= MENU[option]["ingredients"]["coffee"]
    if "milk" in MENU[option]["ingredients"]:
        milk = resources["milk"] >= MENU[option]["ingredients"]["milk"]
    else:
        milk = True
    return [water, coffee, milk]


# TODO Print there is not enough
def not_enough(water, coffee, milk=True):
    resources = {"water": water, "coffee": coffee, "milk": milk}
    if not water or not coffee or not milk:
        for ingredient in resources.keys():
            enough_ingredient = resources[ingredient]
            if not enough_ingredient:
                print(f"Sorry, there's not enough {ingredient}")
                break


# TODO Process coins
def process_coins():
    print("Please insert coins.")
    quarters = int(input("how many quarters? ")) * 0.25
    dimes = int(input("how many dimes? ")) * 0.10
    nickles = int(input("how many nickles? ")) * 0.05
    pennies = int(input("how many pennies? ")) * 0.01
    return quarters + dimes + nickles + pennies


# TODO Check transaction successful
def transaction_successful(money, decision, menu, profits, cost):
    global resources
    if money < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    profits += cost
    resources["water"] -= menu[decision]["ingredients"]["water"]
    resources["coffee"] -= menu[decision]["ingredients"]["coffee"]
    if "milk" in menu[decision]["ingredients"]:
        resources["milk"] -= menu[decision]["ingredients"]["milk"]
    if money > cost:
        print(f"Your change is {round(money-cost,0)}")
    print(f"Here's your {decision}")
    return profits


# TODO Coffee Machine
def coffee_machine():
    on = True
    profits = 0
    while on:
        option = ask_user()
        if option == "report":
            print_report(resources, profits)
        elif option == "turn off":
            on = False
        elif option in ["espresso", "latte", "cappuccino"]:
            enough_resources = check_resources(resources, option, MENU)
            water = enough_resources[0]
            coffee = enough_resources[1]
            try:
                milk = enough_resources[2]
            except:
                milk = False
            if False in enough_resources:
                if not milk:
                    not_enough(water, coffee)
                else:
                    not_enough(water, coffee, milk)
            else:
                money = process_coins()
                cost = MENU[option]["cost"]
                profits += transaction_successful(money, option, MENU, profits, cost)


coffee_machine()

