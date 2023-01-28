import random


def limits():
    problem = str
    solutionSend = str
    equation = random.randint(1, 3)
    if equation == 1:
        n = random.randint(10, 20)
        if (random.choice([-1, 1]) < 0):
            problem = "\lim_{x\\to\:-" + str(n) + "}\left(\\frac{" + str(n-1) + "-\sqrt{x^2-" + str((pow(n, 2) - pow(n-1, 2))) + "}}{x+" + str(n) + "}\\right)"
        else:
            problem = "\lim_{x\\to\:" + str(n) + "}\left(\\frac{" + str(n-1) + "-\sqrt{x^2-" + str((pow(n, 2) - pow(n - 1, 2))) + "}}{x-" + str(n) + "}\\right)"
        solutionSend = problem.replace("\lim", "lim").replace("+", "%2B")
    if equation == 2:
        n = random.randint(1, 9)
        if (random.choice([-1, 1]) < 0):
            problem = "\lim_{x\\to\:-" + str(n) + "}\left(\\frac{x^2-" + str(pow(n, 2)) + "}{x+" + str(n) + "}\\right)"
        else:
            problem = "\lim_{x\\to\:" + str(n) + "}\left(\\frac{x^2-" + str(pow(n, 2)) + "}{x-" + str(n) + "}\\right)"
        solutionSend = problem.replace("\lim", "lim").replace("+", "%2B")
    if equation == 3:
        n = random.randint(1, 9)
        n2 = n * random.choice([-1, 1])
        if (random.choice([-1, 1]) < 0):
            problem = "\lim_{x\\to\:-" + str(n) + "}\left(\\frac{x^2-" + str(pow(n, 2)) + "}{\left(x-" + str(n2) + "\\right)\left(x" + str(random.choice(["+", "-"])) + str(random.randint(1, 9)) + "\\right)}\\right)"
        else:
            problem = "\lim_{x\\to\:" + str(n) + "}\left(\\frac{x^2-" + str(pow(n, 2)) + "}{\left(x-" + str(n2) + "\\right)\left(x" + str(random.choice(["+", "-"])) + str(random.randint(1, 9)) + "\\right)}\\right)"
        solutionSend = problem.replace("\lim", "lim").replace("+", "%2B")
    if equation == 4:
        n = random.randint(1, 3)
        problem = "\lim _{x\\to \infty \:}\left(\left(" + str(n) + "+" + str(n+1) + "x\\right)^{\\frac{" + str((n*random.randint(1, 3) + 1)) + "}{" + str(n+1) + "\ln \left(x\\right)}}\\right)"
        solutionSend = problem.replace("\lim", "lim").replace("+", "%2B")
    return problem, solutionSend


def derivatives():
    problem = str
    solutionSend = str
    equation = random.randint(1, 5)
    solvex = ",\:x=\\frac{\pi}{2}"
    if equation == 1:
        n = random.randint(4, 9)
        problem = ("\\frac{d}{dx}\left(\\frac{" + str(n) + "+\ln\left(x\\right)}{" + str(n) + "-\ln\left(x\\right)}\\right)")
        solutionSend = problem.replace("+", "%2B").replace("=", "%3D")
    if equation == 2:
        if bool(random.getrandbits(1)):
            n, n2 = (random.choice(["cos", "sin", "tan", "sec", "csc", "cot"]) for x in range(2))
            n31 = random.choice([2, 3, 4, 6])
            n32 = random.choice([2, 3, 4, 6])
            while n32 == n31:
                n32 = random.choice([2, 3, 4, 6])
            n3 = (",\:x=\\frac{" + str(n32) + "\\pi}{" + str(n31) + "}")
        else:
            n, n2 = (random.choice(["cos", "sin", "tan", "arccos", "arcsin", "arctan", "sec", "csc", "cot"]) for x in range(2))
            n3 = ""
        problem = ("\\frac{d}{dx}\left(" + str(n) + "\left(" + str(n2) + "\left(x\:\\right)\\right)\\right)" + n3)
        solutionSend = problem.replace("+", "%2B").replace("=", "%3D")
    if equation == 3:
        n = random.choice(["arccos", "arcsin", "arctan"])
        n2 = random.randint(2, 4)
        n4 = random.randint(4, 9)
        problem = ("\\frac{d}{dx}\left(" + str(n4) + "x^" + str(n2) + "\\" + n + "\left(" + str(n4) + "x^" + str(n2) + "\\right)+\sqrt{1-" + str(pow(n4, 2)) + "x^" + str(n2*2) + "}\\right)")
        solutionSend = problem.replace("+", "%2B").replace("=", "%3D")
    if equation == 4:
        n = random.randint(2, 5)
        n2 = random.choice(["cos", "sin", "tan", "arccos", "arcsin", "arctan", "sec", "csc", "cot"])
        if bool(random.getrandbits(1)):
            n31 = random.choice([2, 3, 4, 6])
            n32 = random.choice([2, 3, 4, 6])
            while n32 == n31:
                n32 = random.choice([2, 3, 4, 6])
            n3 = (",\:x=\\frac{" + str(n32) + "\\pi}{" + str(n31) + "}")
        else:
            n3 = ""
        problem = ("\\frac{d}{dx}\left(e^{\\frac{" + str(n+1) + "}{" + str(n) + n2 + "\left(x\\right)}}\\right)" + n3)
        solutionSend = problem.replace("+", "%2B").replace("=", "%3D")
    if equation == 5:
        n, n2 = (random.choice(["cos", "sin", "tan", "sec", "csc", "cot"]) for x in range(2))
        if bool(random.getrandbits(1)):
            n31 = random.choice([2, 3, 4, 6])
            n32 = random.choice([2, 3, 4, 6])
            while n32 == n31:
                n32 = random.choice([2, 3, 4, 6])
            n3 = (",\:x=\\frac{" + str(n32) + "\\pi}{" + str(n31) + "}")
        else:
            n3 = ""
        while n2 == n:
            n2 = random.choice(["cos", "sin", "tan", "sec", "csc", "cot"])
        problem = ("\\frac{d}{dx}\left(\\frac{" + str(n) + "\left(x\\right)\:" + str(random.choice(["+", "-"])) + "\:" + str(n2) + "\left(x\\right)}{" + str(n) + "\left(x\\right)}\\right)" + n3)
        solutionSend = problem.replace("+", "%2B").replace("=", "%3D")
    return problem, solutionSend


def integrals():
    problem = str
    solutionSend = str
    type = random.randint(1,2) #usub, IBP, trig sub
    if (type == 1): #usub. implement definite integrals later.
        a = random.randint(1,5)
        subtype = random.randint(1,2)
        if (subtype == 1):
            problem = "\int\\frac{\left(x^"+str(a)+"\\right)}{1+x^"+str(a+1)+"}dx"
        if (subtype == 2):
            problem = "\int\\frac{x}{1+x^"+str(a+1)+"}dx"
        solutionSend = problem.replace("+", "%2B")
    if (type == 2): #trig sub. add definite integrals later
        subtype = random.randint(1,3)
        a = pow(random.randint(1,6), 2)
        if (subtype == 1):
            problem = "\int\sqrt{x^2+"+str(a)+"}dx"
        if (subtype == 2):
            problem = "\int\sqrt{x^2-"+str(a)+"}dx"
        if (subtype == 3):
            problem = "\int\sqrt{"+str(a)+"-x^2}dx"
        solutionSend = problem.replace("+", "%2B")
    return problem, solutionSend
