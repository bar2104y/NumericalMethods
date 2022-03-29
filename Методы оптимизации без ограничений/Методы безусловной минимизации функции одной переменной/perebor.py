# Метод золотого сечения
import math
import numpy as np


def my_function(x):
    return 2*math.sin(2*x) - 3*math.cos(x) + math.sin(x)


def Gold(f, a, b, eps=1e-1):
    print('\\begin{table}[H] \n'
          '\\begin{center} \n'
          '\\caption{Минимизация методом перебора} \n'
          '\\begin{tabular}{||c|c|c||} \\hline \n'
          'Шаг & $x$ & $f(x)$ \\\\ \n'
          '\\hline')

    line = np.linspace(a,b, int(1/eps))
    k = 0
    for i in line:
        k +=1
        print('{:3} & {:.3f} & {:.3f}\\\\'.format(k, i, f(i)))


    print('\\hline'
          '\\end{tabular}\n'
          '\\end{center} \n'
          '\\end{table} ')

    return line.min(),


if __name__ == "__main__":
    print(Gold(my_function, -1.5, -2.0))
