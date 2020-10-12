'''
Name: Shijie Liu
NUID: 001561546
Course: CS 5001
Course Number: 18529
Semester: Fall 2020

The code is for determining whether the string is a palindrome.
'''


def is_palindrome(raw_str):
    '''
        Function - is_palindrome
            Determines whether the string is a palindrome, which is any string
            that reads the same backwards and forwards, ignoring letter case
            and spaces and is at least 2 characters in length.
        Parameters:
            raw_str -- A string that can include non-letters, such as
            punctuation and numbers.
        Returns:
            The boolean value of whether the string is a palindrome
    '''
    normalized_str = raw_str.replace(" ","").lower()
    is_a_palindrome = (len(normalized_str) >= 2 and
                       normalized_str[::-1] == normalized_str)
    if is_a_palindrome:
        return True
    return False


def main():
    print(is_palindrome("madam  Im adam"))
    print(is_palindrome("a"))
    print(is_palindrome("RAdar"))
    print(is_palindrome("!radar!"))


if __name__ == "__main__":
    main()
