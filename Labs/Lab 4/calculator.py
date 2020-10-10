'''
Name: Shijie Liu
NUID: 001561546
Course Number: 18533
Semester: Fall 2020

This code is for performing basic arithmetic.
'''


def calculate_subtotal(num1, operator, num2):
    '''
        Function - calculate_subtotal
            Calculates the subtotal of two numbers
        Parameters:
            num1 -- The number before the operator
            operator -- A arithmetic operator. Assumes the operator is among
            "+", "-", "*" and "/"
            num2 -- The number after the operator
        Returns:
            The subtotal after performing the requested operation.
    '''
    if operator == "+":
        subtotal = num1 + num2
    elif operator == "-":
        subtotal = num1 - num2
    elif operator == "*":
        subtotal = num1 * num2
    elif operator == "/":
        subtotal = num1 / num2
    return subtotal


def judgement_of_quitting(user_in):
    '''
        Function - judgement_of_quitting
            Determines whether the loop is requested to quit
        Parameters:
            user_in -- The user's input. Assumes the input is "Q", "q", or
            inputs of basic arithmetic in specified format  
        Returns:
            The boolean value of whether to quit the loop
    '''
    QUIT_FLAG = "Q"
    
    should_quit = user_in.upper() == QUIT_FLAG
    if should_quit:
        return False
    return True


def main():
    PROMPT = "Enter the next step in the calculation: "

    initial_value = float(input("Enter a number: "))
    step2 = input(PROMPT)
    while judgement_of_quitting(step2):
        operator, num_str = step2.split()
        value = float(num_str)
        subtotal = calculate_subtotal(initial_value, operator, value)
        print("Subtotal =", subtotal)
        initial_value = subtotal
        step2 = input(PROMPT)
    print("Total =", subtotal)


if __name__ == "__main__":
    main()
