'''
Name: Shijie Liu
NUID: 001561546
Course Number: 18533
Semester: Fall 2020

This code is for a buzzfeed-style quiz that tells users what fruit they would 
be if they were a kind of fruit based on three questions.
'''


def main():
    INVAILD_ANS_WARNING ="Invalid answer. It has automatically changed to A"

    print("Please enter A, B or C for your answer.")
    answer1 = input("What is your favorite sport? " +
                    "A--Soccer. B--Badminton. C--Surfing. " +
                    "Your answer: ").upper()
    if not (answer1 == "A" or answer1 == "B" or answer1 == "C"):
        print(INVAILD_ANS_WARNING)
        answer1 = "A"
    answer2 = input("What is your mush-have food? " +
                    "A--Seafood. B--Steak. C--Salad. " +
                    "Your answer: ").upper()
    if not (answer2 == "A" or answer2 == "B" or answer2 == "C"):
        print(INVAILD_ANS_WARNING)
        answer2 = "A"
    answer3 = input("What is your favorite vacation place? " + 
                    "A--Forest. B--Beach. C--Theme park. "
                    "Your answer: ").upper()
    if not (answer3 == "A" or answer3 == "B" or answer3 == "C"):
        print(INVAILD_ANS_WARNING)
        answer3 = "A"

    is_pomegranate = answer1 == "A" and answer2 == "A" and answer3 == "A"
    is_coconut = answer1 == "A" and answer2 == "A" and answer3 == "B"
    is_watermelon = answer1 =="A" and answer2 == "A" and answer3 == "C"
    is_apple = answer1 == "A" and answer2 == "B"
    is_pear = answer1 == "A" and answer2 == "C"
    is_grape = answer1 == "B"
    is_orange = answer1 == "C" and answer2 == "A" and answer3 == "A"
    is_pineapple = answer1 == "C" and answer2 == "A" and answer3 == "B"
    is_avocado = answer1 == "C" and answer2 == "A" and answer3 == "C"
    is_peach = answer1 == "C" and answer2 == "B"

    if is_pomegranate:
        print("You would be the pomegranate.")
    elif is_coconut:
        print("You would be the coconut.")
    elif is_watermelon:
        print("You would be the watermelon.")
    elif is_apple:
        print("You would be the apple.")
    elif is_pear:
        print("You would be the pear.")
    elif is_grape:
        print("You would be the grape.")
    elif is_orange:
        print("You would be the orange.")
    elif is_pineapple:
        print("You would be the pineapple.")
    elif is_avocado:
        print("You would be the avacado.")
    elif is_peach:
        print("You would be the peach.")
    else:
        print("You would be the strawberry.")


if __name__ == "__main__":
    main()
