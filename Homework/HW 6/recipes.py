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
                    name_of_recipe, ingred_lst, time_string, direction)
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
    '''
        Function -- ingredient_validator
            Checks that a list of ingredients must contain at least one
            non-empty string.
        Parameter:
            item_lst -- A list of ingredients
        Raises:
            ValueError -- If the list of ingredients contain less than one
            non-empty string.
        Returns:
            Nothing
    '''
    MIN_VALID_STR = 1

    bool_sum = 0
    for item in item_lst:
        bool_sum += not_empty_string(item)
        if bool_sum < MIN_VALID_STR:
            raise ValueError


def ingredient_processor(ingredients):
    '''
        Function -- ingredient_processor
            Splits a string of ingredients into a list and remove leading or
            trailing whitespace from each item.
        Parameter:
            ingredients -- A string of ingredients
        Returns:
            The list of ingredients after processing each item.
    '''
    ingredient_lst = ingredients.split(",")
    for i, item in enumerate(ingredient_lst):
        ingredient_lst[i] = item.strip()
    return ingredient_lst


def not_empty_string(string):
    '''
        Function -- not_empty_string
            Checks if the give string is not a empty string.
        Parameter:
            string -- A string to check
        Returns:
            True if the string is not empty, False otherwise.
    '''
    return len(string) != 0


def time_validator(time):
    '''
        Function -- time_validator
            Checks that time is greater than or equal to 0.
        Parameter:
            time -- time to check.
        Raises:
            ValueError -- If the time is less than 0.
        Returns:
            Nothing
    '''
    if time < 0:
        raise ValueError


def create_filename(recipe_name):
    '''
        Function -- create_filename
            Creates a filename using the recipe name.
        Parameter:
            recipe_name -- A recipe name
        Returns:
            The filename from the recipe name
    '''
    UNDERSCORE = "_"
    WHITESPACE = " "
    SUFFIX = ".txt"
    temp_name = recipe_name.lower().strip().replace(WHITESPACE, UNDERSCORE)
    filename = removal(temp_name) + SUFFIX
    return filename


def removal(string):
    '''
        Function -- removal
            Removes any remaining non-alphanumeric characters except for
            underscores from a string.
        Parameter:
            string -- A string
        Returns:
            The string without non-alphanumeric characters.
    '''
    new_str = ""
    for character in string:
        if character.isalnum() or character == "_":
            new_str += character
    return new_str


def filename_validator(filename):
    '''
        Function -- filename_validator
            Checks that a filename is not just ".txt".
        Parameter:
            filename -- A filename to check
        Raises:
            ValueError -- If the filename is just ".txt".
        Returns:
            Nothing
    '''
    EMPTY_NAME = ".txt"
    if filename == EMPTY_NAME:
        raise ValueError


def create_content_lst(recipe_name, ingred_lst, entered_time, direction):
    '''
        Function -- create_content_lst
            Creates a list of content in the required format based on the
            user's input.
        Parameters:
            recipe_name -- The recipe name that the user enters
            ingred_lst -- The list of ingredients
            entered_time -- The time that the user enters
            direction -- The direction that the user enters
        Returns:
            A list of content in the required format.
    '''
    NEWLINE = "\n"
    INGRED_SUBTITLE = "Ingredients:"
    DIRECTION_SUBTITLE = "Directions:"

    time_content = "Time: " + entered_time + " minutes"
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
    '''
        Function -- write_recipe
            Writes a recipe to a file.
        Parameters:
            content -- A list of content to write
            filename -- A string file path
        Returns:
            None. This function does not return.
    '''
    with open(filename, "w") as file:
        file.writelines(content)


def read_recipe(path):
    '''
        Function -- read_recipe
            Reads the entire file of a recipe.
        Parameter:
            path -- A string file path
        Returns:
            The whole content of recipe in the file.
    '''
    file = open(path, "r")
    content = file.read()
    file.close()
    return content


if __name__ == "__main__":
    main()
