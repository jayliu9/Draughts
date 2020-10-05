'''
Name: Shijie Liu
NUID: 001561546
Course: CS 5001
Course Number: 18529
Semester: Fall 2020

The code is for finding a size for a T-shirt company based
on the user's chest measurement. (The code is based on fixing the typo.)
'''
INCREASE_KID_AND_WOMEN = 2
INCREASE_MEN = 3
NO_MATCHING = "not available"


def size_rank(chest_measurement, increase, min_chest):
    '''
        Function -- size_rank
            Represents the level of chest measurement in a size chart in
            proportional form.
        Parameter:
            chest_measurement -- The chest measurement
            increase -- The consistent difference in inches between two
            adjacent sizes in a size chart.
            min_chest -- The minimum inches of chest in a size chart. 
        Returns:
            The level of chest measurement in size charts in proportional form.
    '''
    chest_m_level = (chest_measurement - min_chest) / increase
    return chest_m_level


def size_finder(lvl_of_chest_m):
    '''
        Function -- size_finder
            Determines the size based on the level of chest measurement.
        Parameter:
            lvl_of_chest_m -- The level of chest measurement.
        Returns:
            The size.
    '''
    MINIMUM = 0
    MAX_S_LEVEL = 1
    MAX_M_LEVEL = 2
    MAX_L_LEVEL = 3
    MAX_XL_LEVEL = 4
    MAX_XXL_LEVEL = 5
    MAX_XXXL_LEVEL = 6

    is_s_lvl = lvl_of_chest_m >= MINIMUM and lvl_of_chest_m < MAX_S_LEVEL
    is_m_lvl = lvl_of_chest_m >= MAX_S_LEVEL and lvl_of_chest_m < MAX_M_LEVEL
    is_l_lvl = lvl_of_chest_m >= MAX_M_LEVEL and lvl_of_chest_m < MAX_L_LEVEL
    is_xl_lvl = lvl_of_chest_m >= MAX_L_LEVEL and lvl_of_chest_m < MAX_XL_LEVEL
    is_xxl_lvl = (lvl_of_chest_m >= MAX_XL_LEVEL and
                  lvl_of_chest_m < MAX_XXL_LEVEL)
    is_xxxl_lvl = (lvl_of_chest_m >= MAX_XXL_LEVEL and
                   lvl_of_chest_m < MAX_XXXL_LEVEL)

    if is_s_lvl:
        size = "S"
    elif is_m_lvl:
        size = "M"
    elif is_l_lvl:
        size = "L"
    elif is_xl_lvl:
        size = "XL"
    elif is_xxl_lvl:
        size = "XXL"
    elif is_xxxl_lvl:
        size = "XXXL"
    else:
        size = NO_MATCHING 
    return size


def main():
    INCREASE_KID_AND_WOMEN = 2
    INCREASE_MEN = 3
    MIN_CHEST_KID = 26
    MIN_CHEST_WOMEN = 30
    MIN_CHEST_MEN = 34
    MAX_CHEST_MEN = 52

    chest = float(input("Chest measurement in inches: "))
    if chest < MIN_CHEST_KID or chest >= MAX_CHEST_MEN:
        print("Sorry, we don’t carry your size")
    else:
        level_in_kids = size_rank(chest, INCREASE_KID_AND_WOMEN, MIN_CHEST_KID)
        level_in_women = size_rank(chest, INCREASE_KID_AND_WOMEN,
                                  MIN_CHEST_WOMEN)
        level_in_men = size_rank(chest, INCREASE_MEN, MIN_CHEST_MEN)
        size_in_kids = size_finder(level_in_kids)
        size_in_women = size_finder(level_in_women)
        size_in_men = size_finder(level_in_men)
        if size_finder(level_in_kids) == "XXXL":
            size_in_kids = NO_MATCHING
        print("Your size choice:")
        print("Kids size:", size_in_kids)
        print("Womens size:", size_in_women)
        print("Mens size:", size_in_men)


if __name__ == "__main__":
    main() 
