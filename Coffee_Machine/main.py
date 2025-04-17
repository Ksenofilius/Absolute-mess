# key points: 3 hot flavours, coins operate, automatic cup dispenser, counting cup selling
# analytic table: water inlet, coin slot, coin acceptor, LCD display, drink1, drink2, drink3 [buttons], +, -, menu, drink outlet, waste water box

# 1. 3 hot flavours: 
# #1 espresso - 50ml water, 18mg coffee / $1.50
# #2 latte - 200ml water, 24g coffee, 150ml milk / $2.50
# #3 cappuccino - 250ml water, 24g coffee, 100ml milk / $3.00

# Resources:
# Water - 300ml in the tank               
# Milk - 200ml in the tank
# Coffee - 100g in the tank

# 2. coin operated:
# Penny = 1 cent / $0.01
# Nickel = 5 cents / $0.05
# Dime = 10 cents / $0.10
# Quarter = 25 cents / $0.25


# Program requirements:
# 1. Print a report - tell us what resources the coffee machine has got left 
# 2. Check if resources are sufficient - it needs to update the amounts of resources stored in each of the tanks
# It should give you a message that there is not enough resource for your request if you've orderd something that requires more of one of them
# 3. Process coins - ask the user to insert coins and ask them for each of four types; calculate the total amount of inserted coins and calculate the change
# 4. Check if transtaction is successful
# 5. If transaction was successful then make the selected coffee; remove the reousorces that are required to majke the selected coffee from the tank
# and update the resources
# After there are no resources just end it with a message that thare are none left
####################################################################################
# TODO: Make this project and check the requirements list
# TODO: "What would you like?" | turn off machine with "off"
# TODO: "report" to display resources in the machine
# TODO: if resources are insufficient display: sorry there is not enough <resource>
# TODO: Insert coions (quarters, dimes, nickles, pennies) / everything has its price | if not enough money, refund that and start from the beginning
# quarter = 0.25$ | dime = 0.10$ | nickle = 0.05$ | peny = 0.01$
# TODO: if enough resources and money : remove resources and refund money if necessary
####################################################################################

MENU = {
    # 0
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    # 1
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    # 2
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
    "water": 300, #ml
    "milk": 200, #ml
    "coffee": 100, #g
}
lresources = resources.items()

print("Coffee, coffee, coffee!\n")

# 1. wybierz napój lub wyłącz maszynę

# 2. wyświetl cenę i poproś o monety lub wyświetl poziom zasobów

# 3. usuń zasoby z maszyny, wydaj resztę lub oznajmij brak zasobów

is_on = True
while is_on:
    # choice
    chosen_coffee = input("What coffe do you want? (espresso/latte/cappuccino): ").lower()
        
    # turn off the machine
    if chosen_coffee == "off":
        print("Shutting down...")  
        break

    # raport
    elif chosen_coffee == "report":
        print(resources)

# espresso
if chosen_coffee == "espresso":
    print("Price: $" + str(MENU["espresso"]["cost"]))
    if MENU["espresso"]["ingredients"]["water"] > resources["water"] or  MENU["espresso"]["ingredients"]["coffee"] > resources["coffee"]:
        print("Insufficient resources.")
        is_on = False
    resources["water"] -= MENU["espresso"]["ingredients"]["water"]
    resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]


# latte
elif chosen_coffee == "latte":
    print("Price: $" + str(MENU["latte"]["cost"]))
    if MENU["latte"]["ingredients"]["water"] > resources["water"] or MENU["latte"]["ingredients"]["coffee"] > resources["coffee"] or MENU["latte"]["ingredients"]["milk"] > resources["milk"]: 
        print("Insufficient resources.")
        is_on = False
    resources["water"] -= MENU["latte"]["ingredients"]["water"]
    resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
    resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]


# cappuccino
elif chosen_coffee == "cappuccino":
    print("Price: $" + str(MENU["cappuccino"]["cost"]))
    if MENU["cappuccino"]["ingredients"]["water"] > resources["water"] or MENU["cappuccino"]["ingredients"]["coffee"] > resources["coffee"] or MENU["cappuccino"]["ingredients"]["milk"] > resources["milk"]:
        print("Insufficient resources.")
        is_on = False
    resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
    resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
    resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]




# possible values
rest = 0
sumd = 0
sumd += int(input("How many quarters? ")) * 0.25
sumd += int(input("How many nickles? ")) * 0.1
sumd += int(input("How many dimes? ")) * 0.05
sumd += int(input("How many pennies? ")) * 0.01

# finance calculation
if chosen_coffee == "espresso":
    if sumd - MENU["espresso"]["cost"] == 0:
        profit += sumd
    elif sumd > MENU["espresso"]["cost"]:
        profit += MENU["espresso"]["cost"]
        rest = sumd - MENU["espresso"]["cost"]
    elif sumd < MENU["espresso"]["cost"]:
        print("Need more coins.")

if chosen_coffee == "latte":
    if sumd - MENU["latte"]["cost"] == 0:
        profit += sumd
    elif sumd > MENU["latte"]["cost"]:
        profit += MENU["latte"]["cost"]
        rest = sumd - MENU["latte"]["cost"]
    elif sumd < MENU["latte"]["cost"]:
        print("Need more coins.")

if chosen_coffee == "cappuccino":
    if sumd - MENU["cappuccino"]["cost"] == 0:
        profit += sumd
    elif sumd > MENU["cappuccino"]["cost"]:
        profit += MENU["cappuccino"]["cost"]
        rest = sumd - MENU["cappuccino"]["cost"]
    elif sumd < MENU["cappuccino"]["cost"]:
        print("Need more coins.")

print(f"Your rest: $" + str(round(rest, 3)))
    
while input("Do you want another coffee?\nType 'yes' or 'no': ").lower() == "no":
    mhm = False
    break


    


















