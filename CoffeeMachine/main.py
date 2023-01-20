''' Creating a script for a coffee machine that
 - takes order from the user
 - checks if there is enough resources
 - checks if enough money was inserted
 - if all conditions are met, machine prepares the ordered coffee and return money
 - also machine is able to pprint report of the current resources available

'''


# creating a menu for the machine to use
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

# creating a resources for the machine to use
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

# TODO 1:  print a report
def report(resources_left):
    print(f" Water: {resources_left['water']}")
    print(f" Coffee: {resources_left['coffee']}")
    print(f" Milk: {resources_left['milk']}")
    print(f" Money: {resources_left['money']}")


# TODO 2: check if resources are sufficient to make a drink
def check_resources(resources_left, coffee):
    #print(f"inside check_resources inputs{resources_left}, {coffee}")
    if MENU[coffee]["ingredients"]["water"] > resources_left["water"]:
        return "Sorry not enough water"
    elif MENU[coffee]["ingredients"]["coffee"] > resources_left["coffee"]:
        return "Sorry not enough coffee"
    elif "milk" in MENU[coffee]["ingredients"]:
        if MENU[coffee]["ingredients"]["milk"]> resources_left["milk"]:
            return "Sorry not enough milk"
        return "ok"
    else:
        return "ok"


# TODO 3: check if amount of money is sufficient
def check_money(money_inserted, order):
    if MENU[order]["cost"] == money_inserted:
        return "ok"
    if MENU[order]["cost"] < money_inserted:
        cost=MENU[order]["cost"]
        print(f"Here is your change {money_inserted-cost:.02f}$")
        return "ok"
    else:
        print("not sufficient amount. Money refunded.")
        return "not ok"

# TODO 4: deduct resources
def deduct_resources(order1, current_resources):
    current_resources["water"] = current_resources["water"] - MENU[order1]["ingredients"]["water"]
    current_resources["coffee"] = current_resources["coffee"] - MENU[order1]["ingredients"]["coffee"]
    if "milk" in MENU[order1]["ingredients"]:
        current_resources["milk"] = current_resources["milk"] - MENU[order1]["ingredients"]["milk"]
    return current_resources


def coffeemachine(resources_left):
    Turnoff = False
    #print(resources_left)
    while not Turnoff:
        order = input("What would you like to drink - espresso, latte or cappuccino? ")
        if order == "report":
            report(resources_left)
        elif order == "off":
            Turnoff = True
        else:
            ok = check_resources(resources_left, order)
            #print(f"function check_resources returns{ok}")
            if ok == "ok":
                print("Please insert coins")
                quarters = int(input("How many quarters? "))
                dimes = int(input("How many dimes? "))
                nickels = int(input("How many nickels? "))
                pennies = int(input("How many pennies? "))
                total = 0.01 * pennies + 0.05 * nickels + 0.1 * dimes + 0.25 * quarters
                money = check_money(total, order)
                if money == "ok":
                    resources_left = deduct_resources(order, resources_left)
                    cost = MENU[order]["cost"]
                    #print(resources_left)
                    resources_left["money"] += cost
                    print(f"Here is your {order}. Enjoy!")
                    #print(resources_left)


coffeemachine(resources)







