import numpy as np
import matplotlib.pyplot as plt
import math
def example_function1(x):
    return math.fabs(x)
def example_function2(x):
    return 1/(1 + 25 * x**2)
def Chebyshev(f, n):
    x_array = []
    for i in range(n):
        x_value = math.cos(((2 * i + 1) * math.pi) / (2 * n))
        x_array.append(x_value)
    y_array = [f(x) for x in x_array]
    return x_array, y_array
def interp(f, n):
    x_array = np.linspace(-1, 1, n)
    y_array = [f(x) for x in x_array]
    return x_array, y_array
def Lagrange(f, n, x):
    x_array, y_array = Chebyshev(f, n)
    result = 0.0
    for i in range(n):
        p = 1.0
        for j in range(n):
            if j != i:
                p *= (x - x_array[j]) / (x_array[i] - x_array[j])
        result += p * y_array[i]
    return result

n = int(input("Введите количество точек (n): "))
a = -1
b = 1
x_values = np.linspace(a, b, 100)
y_values1 = [example_function2(x) for x in x_values]
y_values2 = [Lagrange(example_function2, n, x) for x in x_values]
fig, ax = plt.subplots()
ax.plot(x_values, y_values1, label='f(x) = 1/(1 + 25*x^2)', color='blue')
ax.plot(x_values, y_values2, label='Интерполяция Лагранжа', color='red')
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title('График функции и интерполированного полинома')
ax.legend()
plt.grid()
plt.show()
