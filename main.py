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


# Todo: 2: def coffee_machine => while on loop
def coffee_machine(menu_data, current_resources):
    available_options = coffee_options_checker(menu_data, current_resources)
    no_of_available_options = len(available_options)
    if no_of_available_options > 1:
        print("Which coffee would you like ?")
        for coffee_type in available_options:
            print(coffee_type, end=" ")
        user_choice = input()

    return


# Todo: 3: check resources and show available options
# Todo: 4: get user choice
# Todo: 5: is off => return

# Todo: 6: is not off => def money
# Todo: 7: Make Coffee.
# Todo: 8: Add resources


coffee_machine(MENU, resources)
