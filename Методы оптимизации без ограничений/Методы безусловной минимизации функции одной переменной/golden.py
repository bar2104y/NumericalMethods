# Метод золотого сечения
import math


def square(x, a=1, b=0, c=0):
    return a * x * x + b * x + c


def Gold(f, a, b, eps=1e-3):
    tau = (-1 + math.sqrt(5)) / 2

    while abs(a - b) > eps:
        x1 = a + (b - a) * tau
        x2 = a + (b - a) * (1 - tau)

        if f(x1) > f(x2): b = x1
        else: a = x2

    return (a + b) / 2


if __name__ == "__main__":
    print(Gold(square, -5, 10))
