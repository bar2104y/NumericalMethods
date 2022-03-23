# Метод перебора

def square(x, a=1, b=0, c=0):
    return a*x*x + b*x + c

def enumeration(f, a, b, eps=0.01):
    step = eps / 2
    current = a+step
    minx = a
    minvalue = f(a)

    while current <= b:
        # print("x:", current, "y:", f(current))
        if f(current) < minvalue:
            minvalue = f(current)
            minx = current

        current += step

    return minx, minvalue


if __name__ == "__main__":
    print(enumeration(square, -5, 10))