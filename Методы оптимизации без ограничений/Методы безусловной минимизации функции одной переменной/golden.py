# Метод золотого сечения
import math


def my_function(x):
    return 2*math.sin(2*x) - 3*math.cos(x) + math.sin(x)


def Gold(f, a, b, eps=1e-2):
    print('\\begin{table}[H] \n'
          '\\begin{center} \n'
          '\\caption{Минимизация методом золотого сечения} \n'
          '\\begin{tabular}{||c|c|c|c|c|c|c||} \n'
          '\\hline'
          'Шаг & $x_1$ & $x_2$ &  $f(x_1)$& $f(x_2)$&a&b \\\\'
          '\\hline')

    # Коэффициент tau - отношение золотого сечения
    tau = (-1 + math.sqrt(5)) / 2

    i = 0
    while abs(a - b) > eps:
        x1 = a + (b - a) * tau
        x2 = a + (b - a) * (1 - tau)

        if f(x1) > f(x2):
            b = x1
        else:
            a = x2

        print('{:3}&{:.3f}&{:.3f}&{:.3f}&{:.3f}&{:.3f}&{:.3f}\\\\'.format(i, x1, x2, f(x1), f(x2),a,b))
        i += 1

    print('\\hline'
          '\\end{tabular}\n'
          '\\end{center} \n'
          '\\end{table} ')

    return (a + b) / 2, f((a + b) / 2)


if __name__ == "__main__":
    print(Gold(my_function, -1.5, 2.0))
