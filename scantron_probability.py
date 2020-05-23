"""
This is to test whether it is better to select answers randomly in a multiple choice test, or to guess all with the same answer.
"""

length = 1000000
solutions = ["A", "B", "C", "D"]
import random

solutionList = [random.choice(solutions) for x in range(length)]
answerList = [random.choice(solutions) for x in range(length)]
constant_answerList = ["C" for x in range(length)]

def compare(lhs, rhs):
    percentage = len([(x, y) for x, y in (zip(lhs, rhs)) if x == y]) / length * 100
    return percentage

print('Percent correct for random answers: ', compare(solutionList, answerList), '%', sep = '')
print('Percent correct for only "C": ', compare(solutionList, constant_answerList), '%', sep = '')