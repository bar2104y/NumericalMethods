# Метод дихотомии

def square(x, a=1, b=0, c=0):
    return a*x*x + b*x + c

def dichotomy(f, a, b, eps=0.01):
    while abs(b-a) > eps:
        c = (a+b)/2