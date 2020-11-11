'''
Name: Shijie Liu
NUID: 001561546
Course: CS 5001
Course Number: 18529
Semester: Fall 2020

The code is a program that enable users to save and read recipes.
'''


def main():
    PROMPT_MENU = "MENU: 1 - Save a new recipe, 2 - Read a recipe, 3 - Quit "
    PROMPT_INGRED = ("Enter the ingredients on one line. Separate each " +
                     "ingredient with a comma. ")
    PROMPT_DIRECTION = "Enter the directions (1 paragraph only): "
    PROMPT_TIME = "Enter the time needed in minutes: "
    PROMPT_RECIPE = "Enter a name for the recipe: "
    PROMPT_FILENAME = ("Enter a string containing only letters, numbers, and" +
                       " spaces ")
    PROMPT_READ = "Enter the name of the recipe: "
    CHOICE_SAVE = "1"
    CHOICE_READ = "2"
    QUIT = "3"
    CHOICES = (CHOICE_SAVE, CHOICE_READ, QUIT)

    user_in = input(PROMPT_MENU)
    while user_in != QUIT:
        try:
            if user_in not in CHOICES:
                raise ValueError

            if user_in == CHOICE_SAVE:
                ingredients = input(PROMPT_INGRED)
                valid_ingred = False
                while not valid_ingred:
                    ingred_lst = ingredient_processor(ingredients)
                    try:
                        ingredient_validator(ingred_lst)
                        valid_ingred = True
                    except ValueError:
                        print("Recipe must have at least one ingredient.")
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
                        print("Invalid time. Must be an integer greater than" +
                              " or equal to 0.")
                        time_string = input(PROMPT_TIME)

                name_of_recipe = input(PROMPT_RECIPE)
                filename = create_filename(name_of_recipe)
                try:
                    filename_validator(filename)
                except ValueError:
                    print("Unable to create the filename.")
                    valid_filename = False
                    alternative_name = input(PROMPT_FILENAME)
                    while not valid_filename:
                        filename = create_filename(alternative_name)
                        try:
                            filename_validator(filename)
                            valid_filename = True
                        except ValueError:
                            alternative_name = input(PROMPT_FILENAME)

                recipe_content = create_content_lst(
                    name_of_recipe, ingred_lst, needed_time, direction)
                write_recipe(recipe_content, filename)
                print(name_of_recipe, "recipe saved to", filename)

            elif user_in == CHOICE_READ:
                recipe_to_read = input(PROMPT_READ)
                file_to_open = create_filename(recipe_to_read)
                try:
                    content = read_recipe(file_to_open)
                    print(content)
                except FileNotFoundError:
                    print("Unable to read", file_to_open)
        except ValueError:
            print("Invalid choice.")
        user_in = input(PROMPT_MENU)


def ingredient_validator(item_lst):
    MIN_VALID_STR = 1

    bool_sum = 0
    for item in item_lst:
        bool_sum += not_empty_string(item)
        if bool_sum < MIN_VALID_STR:
            raise ValueError


def ingredient_processor(ingredients):
    ingredient_lst = ingredients.split(",")
    for i, item in enumerate(ingredient_lst):
        ingredient_lst[i] = item.strip()
    return ingredient_lst


def not_empty_string(string):
    return len(string) != 0


def time_validator(time):
    if time < 0:
        raise ValueError


def create_filename(recipe_name):
    UNDERSCORE = "_"
    WHITESPACE = " "
    SUFFIX = ".txt"
    temp_name = recipe_name.lower().strip().replace(WHITESPACE, UNDERSCORE)
    filename = removal(temp_name) + SUFFIX
    return filename


def removal(string):
    new_str = ""
    for character in string:
        if character.isalnum() or character == "_":
            new_str += character
    return new_str


def filename_validator(filename):
    EMPTY_NAME = ".txt"
    if filename == EMPTY_NAME:
        raise ValueError


def create_content_lst(recipe_name, ingred_lst, entered_time, direction):
    NEWLINE = "\n"
    INGRED_SUBTITLE = "Ingredients:"
    DIRECTION_SUBTITLE = "Directions:"

    time_content = "Time: %d minutes" % entered_time
    content_lst = []
    content_lst.append(recipe_name + NEWLINE)
    content_lst.append(NEWLINE)
    content_lst.append(INGRED_SUBTITLE + NEWLINE)
    for item in ingred_lst:
        content_lst.append(item + NEWLINE)
    content_lst.append(NEWLINE)
    content_lst.append(time_content + NEWLINE)
    content_lst.append(NEWLINE)
    content_lst.append(DIRECTION_SUBTITLE + NEWLINE)
    content_lst.append(direction)
    return content_lst


def write_recipe(content, filename):
    with open(filename, "w") as file:
        file.writelines(content)


def read_recipe(path):
    file = open(path, "r")
    content = file.read()
    file.close()
    return content


if __name__ == "__main__":
    main()
