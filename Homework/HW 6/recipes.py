'''
Name: Shijie Liu
NUID: 001561546
Course: CS 5001
Course Number: 18529
Semester: Fall 2020

The code is a program that enable users to save and read recipes.
'''
CHOICES = ("1", "2", "3")
PROMPT_MENU = "MENU: 1 - Save a new recipe, 2 - Read a recipe, 3 - Quit"
PROMPT_INGRED = ("Enter the ingredients on one line. Separate each" + 
                 "ingredient with a comma")
PROMPT_DIRECTION = "Enter the direction (1 paragraph only): "
PROMPT_TIME = "Enter the time needed in minutes: "
PROMPT_RECIPE = "Enter the name of the recipe"


def main():
    user_in = input(PROMPT_MENU)
    while user_in not in CHOICES:
        print("Invalid choice")
        user_in = input(PROMPT_MENU)
    
    ingredients = input(PROMPT_INGRED)
    valid_ingred = False
    while not valid_ingred:
        ingred_lst = ingredient_processor(ingredients)
        try:
            ingredient_validator(ingred_lst)
            valid_ingred = True
        except ValueError:
            print("Recipe must have at least one ingredient")
            ingredients = input(PROMPT_INGRED)
    
    direction = input(PROMPT_DIRECTION)
    time_string = input(PROMPT_TIME)
    valid_time = False
    while not valid_time:
        try:
            needed_time = int(time_string)
            time_validator(needed_time)
            valid_time = True
        except ValueError:
            print("Invalid time. Must be an integer greater than or equal to",
                  "0")
            time_string = input(PROMPT_TIME)

    name_of_recipe = input(PROMPT_RECIPE)
            

def ingredient_validator(item_lst):
    MIN_VALID_STR = 1

    bool_sum = 0
    for item in enumerate(item_lst):
        sum += is_empty_string(item)
        if bool_sum < MIN_VALID_STR:
            raise ValueError


def ingredient_processor(ingredients):
    ingredient_lst = ingredients.split(",")
    for i, item in enumerate(ingredient_lst):
        ingredient_lst[i] = item.strip()
    return ingredient_lst


def is_empty_string(string):
    return len(string) == 0


def time_validator(time):
    if time < 0:
        raise ValueError
