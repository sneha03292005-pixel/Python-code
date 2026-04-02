

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
logo = """
    (  )   (   )  )
     ) (   )  (  (
     ( )  (    ) )
     _____________
    <_____________> ___
    |             |/ _ \
    |               | | |
    |               |_| |
 ___|             |\___/
 /    \___________/    \
 \_____________________/
"""

print(logo)



profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

is_on = True
while True:
    print(logo)
    choice=input("What would you like? (espresso/latte/cappuccino): ")
    if choice=="off":
        is_on=False
        break
    elif choice=="report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink=MENU[choice]
        if resources["water"]<drink["ingredients"]["water"]:
            print("Sorry there is not enough water.")
            continue
        if resources["coffee"]<drink["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
            continue
        if choice!="espresso":
            if resources["milk"]<drink["ingredients"]["milk"]:
                print("Sorry there is not enough milk.")
                continue
        print("Please insert coins.")
        quarters=int(input("How many quarters?: "))
        dimes=int(input("How many dimes?: "))
        nickels=int(input("How many nickels?: "))
        pennies=int(input("How many pennies?: "))
        total=quarters*0.25+dimes*0.10+nickels*0.05+pennies*0.01
        if total<drink["cost"]:
            print("Sorry that's not enough money. Money refunded.")
            continue
        elif total>drink["cost"]:
            change=round(total-drink["cost"],2)
            print(f"Here is ${change} in change.")
        profit+=drink["cost"]
        resources["water"]-=drink["ingredients"]["water"]
        resources["coffee"]-=drink["ingredients"]["coffee"]
        if choice!="espresso":
            resources["milk"]-=drink["ingredients"]["milk"]
        print(f"Here is your {choice} ☕️. Enjoy!")