import random


def limits():
    problem = str
    solutionSend = str
    equation = random.randint(1, 3)
    if equation == 1:
        n = random.randint(10, 20)
        n2 = n * random.choice([-1, 1])
        problem = "\lim_{x\\to\:" + str(n2) + "}\left(\\frac{" + str(n-1) + "-\sqrt{x^2-" + str((pow(n, 2) - pow(n-1, 2))) + "}}{x-\left(" + str(n2) + "\\right)}\\right)"
        solutionSend = "lim x to " + str(n2) + " \left(\\frac{" + str(n-1) + "-\sqrt{x^2-" + str((pow(n, 2) - pow(n-1, 2))) + "}}{x-\left(" + str(n2) + "\\right)}\\right)"
    if equation == 2:
        n = random.randint(1, 9)
        n2 = n * random.choice([-1, 1])
        problem = "\lim_{x\\to\:" + str(n2) + "}\left(\\frac{x^2-" + str(pow(n, 2)) + "}{x-" + str(n2) + "}\\right)"
        solutionSend = "lim x to " + str(n2) + "}\left(\\frac{x^2-" + str(pow(n, 2)) + "}{x-" + str(n2) + "}\\right)"
    if equation == 3:
        n = random.randint(1, 9)
        n2 = n * random.choice([-1, 1])
        problem = "\lim_{x\\to\:" + str(n2) + "}\left(\\frac{x^2-" + str(pow(n, 2)) + "}{\left(x-" + str(n2) + "\\right)\left(x-" + str(random.randint(1, 9)*random.choice([-1, 1])) + "\\right)}\\right)"
        solutionSend = "lim x to " + str(n2) + "}\left(\\frac{x^2-" + str(pow(n, 2)) + "}{\left(x-" + str(n2) + "\\right)\left(x-" + str(random.randint(1, 9)*random.choice([-1, 1])) + "\\right)}\\right)"
    return problem, solutionSend


def derivatives():
    problem = str
    solutionSend = str
    equation = 1
    if (equation == 1):
        n, n2 = (random.choice(["cos", "sin", "tan", "arccos", "arcsin", "arctan"]) for x in range(2))
        problem, solutionSend = (("\\frac{d}{dx}\left(" + n + "\left(" + n2 + "\left(x\:\\right)\\right)\\right)") for x in range(2))
    return problem, solutionSend

import random

def limits():
    equation = 1
    if equation == 1:
        n = random.randint(13, 14)
        n2 = n * random.choice([-1, 1])
        n3 = n * abs(n)
        problem = "\lim _{x\\to\:" + str(n2) + "}\left(\\frac{" + str(n-1) + "-\sqrt{x^2-" + str((pow(n, 2) - pow(n-1, 2))) + "}}{x-\left(" + str(n2) + "\\right)}\\right)"
        solutionSend = "lim x to " + str(n2) + " \left(\\frac{" + str(n-1) + "-\sqrt{x^2-" + str((pow(n, 2) - pow(n-1, 2))) + "}}{x-\left(" + str(n2) + "\\right)}\\right)"
        return problem, solutionSend