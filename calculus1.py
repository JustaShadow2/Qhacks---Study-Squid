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