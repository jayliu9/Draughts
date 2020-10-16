'''
Name: Shijie Liu
NUID: 001561546
Course Number: 18533
Semester: Fall 2020

This code is for computing some statistics for a class of students' scores on
an assignment.
'''


def average(scores):
    '''
        Function - average
            Calculates the average of students' scores
        Parameters:
            scores -- A list of the students' scores
        Returns:
            The average of students' scores. If the supplied arguments is a
            empty list, returns 0
    '''
    average_of_scores = 0
    for x in scores:
        average_of_scores += x / len(scores)
    return average_of_scores


def median(scores):
    '''
        Function - median
            Calculates the median of students' scores
        Parameters:
            scores -- A list of the students' scores
        Returns:
            The median of students' scores. If the supplied arguments is a
            empty list, returns 0
    '''
    copied_scores = scores.copy()
    copied_scores.sort()
    if len(copied_scores) == 0:
        return 0
    elif len(copied_scores) % 2 == 0:
        index1 = len(copied_scores) // 2 - 1
        index2 = len(copied_scores) // 2
        score_median = (copied_scores[index1] + copied_scores[index2]) / 2
        return score_median
    else:
        median_index = len(scores) // 2
        score_median = copied_scores[median_index]
        return score_median


def lowest(scores):
    '''
        Function - lowest
            Gets the lowest score among students' scores
        Parameters:
            scores -- A list of the students' scores
        Returns:
            The lowest score of students' scores. If the supplied arguments is
            a empty list, returns 0
    '''
    if len(scores) == 0:
        return 0
    copied_scores = scores.copy()
    copied_scores.sort()
    return copied_scores[0]


def highest(scores):
    '''
        Function - highest
            Gets the highest score among students' scores
        Parameters:
            scores -- A list of the students' scores
        Returns:
            The highest score of students' scores. If the supplied arguments is
            a empty list, returns 0
    '''
    if len(scores) == 0:
        return 0
    copied_scores = scores.copy()
    copied_scores.sort()
    return copied_scores[-1]


def main():
    scores_of_students = [94, 85, 73, 77, 86, 95]
    the_average = average(scores_of_students)
    print("The average of the scores is", the_average)
    the_median = median(scores_of_students)
    print("The median of the scores is", the_median)
    lowest_score = lowest(scores_of_students)
    print("The lowest of the scores is", lowest_score)
    highest_score = highest(scores_of_students)
    print("The highest of the scores is", highest_score)


if __name__ == "__main__":
    main()
