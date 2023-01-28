import random


def limits():
    problem = str
    solutionSend = str
    equation = random.randint(1, 3)
    if equation == 1:
        n = random.randint(10, 20)
        n2 = n * random.choice([-1, 1])
        problem = "\lim_{x\\to\:" + str(n2) + "}\left(\\frac{" + str(n-1) + "-\sqrt{x^2-" + str((pow(n, 2) - pow(n-1, 2))) + "}}{x-\left(" + str(n2) + "\\right)}\\right)"
        solutionSend = problem.replace("\lim", "lim").replace("+", "%2B")
    if equation == 2:
        n = random.randint(1, 9)
        n2 = n * random.choice([-1, 1])
        problem = "\lim_{x\\to\:" + str(n2) + "}\left(\\frac{x^2-" + str(pow(n, 2)) + "}{x-" + str(n2) + "}\\right)"
        solutionSend = problem.replace("\lim", "lim").replace("+", "%2B")
    if equation == 3:
        n = random.randint(1, 9)
        n2 = n * random.choice([-1, 1])
        problem = "\lim_{x\\to\:" + str(n2) + "}\left(\\frac{x^2-" + str(pow(n, 2)) + "}{\left(x-" + str(n2) + "\\right)\left(x-" + str(random.randint(1, 9)*random.choice([-1, 1])) + "\\right)}\\right)"
        solutionSend = problem.replace("\lim", "lim").replace("+", "%2B")
    if equation == 4:
        n = random.randint(1, 3)
        problem = "\lim _{x\\to \infty \:}\left(\left(" + str(n) + "+" + str(n+1) + "x\\right)^{\\frac{" + str((n*random.randint(1, 3) + 1)) + "}{" + str(n+1) + "\ln \left(x\\right)}}\\right)"
        solutionSend = problem.replace("\lim", "lim").replace("+", "%2B")
    return problem, solutionSend


def derivatives():
    problem = str
    solutionSend = str
    equation = random.randint(1, 3)
    if (equation == 1):
        n, n2 = (random.choice(["cos", "sin", "tan", "arccos", "arcsin", "arctan"]) for x in range(2))
        problem, solutionSend = (("\\frac{d}{dx}\left(" + str(n) + "\left(" + str(n2) + "\left(x\:\\right)\\right)\\right)") for x in range(2))
        solutionSend = problem.replace("+", "%2B")
    if (equation == 2):
        n = random.choice(["arccos", "arcsin", "arctan"])
        n2 = random.randint(2, 4)
        n3 = random.randint(4, 9)
        problem = ("\\frac{d}{dx}\left(" + str(n3) + "x^" + str(n2) + "\\" + n + "\left(" + str(n3) + "x^" + str(n2) + "\\right)+\sqrt{1-" + str(pow(n3, 2)) + "x^" + str(n2*2) + "}\\right)")
        solutionSend = problem.replace("+", "%2B")
    if (equation == 3):
        n = random.randint(4, 9)
        problem = ("\\frac{d}{dx}\left(\\frac{" + str(n) + "+\ln\left(x\\right)}{" + str(n) + "-\ln\left(x\\right)}\\right)")
        solutionSend = problem.replace("+", "%2B")
    if (equation == 4):
        n = 3
    return problem, solutionSend

