# Todo: 1: Import resources, screen clear
from data import MENU, resources


def coffee_options_checker(menu_data, current_resources):
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


def money(menu_data,coffee_type):
    total = 0
    cost = menu_data[coffee_type]["cost"]
    print(f"That will be ${cost}")
    while total != cost:
        penny = 0.01
        nickel = 0.05
        dime = 0.1
        quarter = 0.25
        try:
            penny_input = int(input("How many pennies ?: "))
        except:
            penny_input = 0
        try:
            nickel_input = int(input("How many nickels ?: "))
        except:
            nickel_input = 0
        try:
            dime_input = int(input("How many dimes ?: "))
        except:
            dime_input = 0
        try:
            quarter_input = int(input("How many quarters ?: "))
        except:
            quarter_input = 0
        total += round((penny_input*penny)+(nickel_input*nickel)+(dime_input*dime)+(quarter_input*quarter), 2)
        if total > cost:
            change = total - cost
            total = cost
            print(f"here is the balance: ${round(change, 2)}")
        elif total < cost:
            print(f"not enough, you are still missing ${cost-total}")
        else:
            return cost


# Todo: 2: def coffee_machine => while on loop
def coffee_machine(menu_data, current_resources):
    available_options = coffee_options_checker(menu_data, current_resources)
    if available_options:
        user_option = ''
        while user_option not in available_options:
            print("Which coffee would you like ?")
            for coffee_type in available_options:
                print(coffee_type, end=" ")
            user_choice = input()
            if user_choice in available_options:
                current_resources["money"] += money(menu_data, user_choice)
            else:
                print("Invalid choice")
        current_resources = make_coffee(menu_data,current_resources)
    else:
        print("Sorry, we are out of resources")
    return


# Todo: 3: check resources and show available options
# Todo: 4: get user choice
# Todo: 5: is off => return

# Todo: 6: is not off => def money
# Todo: 7: Make Coffee.
# Todo: 8: Add resources


coffee_machine(MENU, resources)
