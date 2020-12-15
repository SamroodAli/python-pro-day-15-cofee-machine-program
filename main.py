from data import MENU, resources
from logo import LOGO


def add_resources(current_resources):
    """"function to add resouces to current resources"""
    for resource in current_resources:
        qty = input(f"Please specify the quantity of {resource} to add : ")
        current_resources[resource] += int(qty) if qty != "" else 0
    return current_resources


def coffee_options_checker(menu_data, current_resources):
    """returns the list of coffee options available with current resources"""
    list_options = []
    for coffee_type in menu_data:
        sufficient = True
        coffee_ingredients_list = menu_data[coffee_type]["ingredients"]
        for ingredient in coffee_ingredients_list:
            if coffee_ingredients_list[ingredient] > current_resources[ingredient]:
                sufficient = False
        if sufficient:
            list_options.append(coffee_type)
    return list_options


def money(menu_data, coffee_type):
    """function to handle money transactions and returns the revenue"""
    total = 0
    cost = menu_data[coffee_type]["cost"]
    print(f"That will be ${cost}")
    while total != cost:
        currency = {
            "pennies": 0.01,
            "nickels": 0.05,
            "dimes": 0.1,
            "quarters": 0.25,
        }
        for coin in currency:
            user_input = input(f"How many {coin} ?: ")
            user_input = int(user_input) if user_input != '' else 0
            total += (currency[coin]*user_input)
        total = round(total,2)
        if total > cost:
            change = total - cost
            total = cost
            print(f"here is the balance: ${round(change, 2)}")
            return cost
        elif total < cost:
            print(f"not enough, you are still missing ${cost - total}")
        else:
            return cost


def reporter(current_resources):
    """prints current resources"""
    print("Current resources report :")
    print(f"Water : {current_resources['water']}ml")
    print(f"Milk :  {current_resources['milk']}ml")
    print(f"Coffee : {current_resources['coffee']}g")
    print(f"Money : ${current_resources['money']}")


def make_coffee(coffee_type, menu_data, current_resources):
    """function to make coffee, takes menu order and deducts needed
     resources from current resources, and prints coffee"""

    print(f"Here is your {coffee_type}, thank you for shopping, visit again.\n")
    ingredients = menu_data[coffee_type]["ingredients"]
    for ingredient in ingredients:
        current_resources[ingredient] -= ingredients[ingredient]
    return current_resources


def coffee_machine(menu_data, current_resources):
    is_on = True
    while is_on:
        print(LOGO)
        available_options = coffee_options_checker(menu_data, current_resources)
        if available_options:
            user_option = ""
            while user_option not in available_options and user_option not in ["add", "report", "off"]:
                print("Which coffee would you like ?")
                for coffee_type in available_options:
                    print(coffee_type, end=" ")
                user_option = input().lower()
                if user_option in available_options:
                    current_resources["money"] += money(menu_data, user_option)
                    current_resources = make_coffee(user_option, menu_data, current_resources)
                elif user_option == 'off':
                    is_on = False
                    return
                elif user_option == "report":
                    reporter(current_resources)
                elif user_option == "add":
                    current_resources = add_resources(current_resources)
                else:
                    print("Invalid choice")
        else:
            is_on = False
            print("Sorry, we are out of resources")
    return


coffee_machine(MENU, resources)
