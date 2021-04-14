"""
File: khansole_academy.py
-------------------------
This program asks the user to answer two digit addition problems.
If answered incorrectly, the correct answer is provided.
The program will continue to ask the user to answer questions until
the user answers three correctly in a row.
"""

import random
NUM_MIN = 10
NUM_MAX = 99
CORRECT_IN_A_ROW = 3

def main():
    # start with no correct answers = 0.
    num_correct = 0

    while num_correct != CORRECT_IN_A_ROW:
        # randomly generate two digit addition problems for the user to solve
        num1 = random.randint(NUM_MIN, NUM_MAX)
        num2 = random.randint(NUM_MIN, NUM_MAX)
        total = num1 + num2

        # ask user to solve problem, while the user has not yet answered 3 correctly in a row
        print("What is " + str(num1) + " + " + str(num2) + "?")
        answer = int(input("Your answer: "))

        # check to see if the problem was answered right or wrong by the user
        if answer == total:
            print("Correct! You've gotten " + str(num_correct + 1) + " correct in a row.")
            num_correct += 1
        else:
            print("Incorrect. The expected answer is " + str(total) + ".")
            num_correct = 0

    # message user receives when three answered correctly in a row:
    print("Congratulations! You mastered addition.")


if __name__ == '__main__':
    main()
