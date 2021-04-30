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
    num_correct = 0

    while num_correct != CORRECT_IN_A_ROW:
        num1 = random.randint(NUM_MIN, NUM_MAX)
        num2 = random.randint(NUM_MIN, NUM_MAX)
        total = num1 + num2

        print("What is", num1, "+", str(num2) + "?")
        answer = int(input("Your answer: "))

        if answer == total:
            print("Correct! You've gotten", (num_correct + 1), "correct in a row.")
            num_correct += 1
        else:
            print("Incorrect. The expected answer is", str(total) + ".")
            num_correct = 0

    print("Congratulations! You mastered addition.")


if __name__ == '__main__':
    main()

