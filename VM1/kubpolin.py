import numpy as np
import matplotlib.pyplot as plt
import math
global_context = {
    'cos': np.cos,
    'sin': np.sin,
    'tan': np.tan,
    'sqrt': np.sqrt,
    'exp': np.exp,
    'log': np.log,
    'pi': math.pi,
    'e': math.e,
}
def function(x_array, func):
    func_vect = np.vectorize(lambda x: eval(func, {"builtins": None, 'x': x}, global_context))
    return func_vect(x_array)
def GetMatrix(x_array,y_array,num,N):
    matrix = np.zeros((N, N))
    h = x_array[1] - x_array[0]
    otherC = np.zeros(N)
    for i in range(1, N - 1):
        matrix[i, i] = 4 * h
        matrix[i, i + 1] = 1 * h
        matrix[i, i - 1] = 1 * h
        otherC[i] = (3 / h) * (y_array[i + 1] - 2 * y_array[i] + y_array[i - 1])
    matrix[0, 0] = 1
    matrix[N - 1, N - 1] = 1
    otherC[0] = 0
    otherC[N - 1] = 0
    c = np.linalg.solve(matrix, otherC)
    return c
def GetIndex(x_array, y_array, num, c):
    coefficient = []
    h = x_array[1] - x_array[0]
    for i in range(num):
        a = y_array[i]
        d = (c[i + 1] - c[i]) / (3 * h)
        b = ((y_array[i + 1] - y_array[i]) / h) - ((2 * c[i] + c[i + 1]) * h / 3)
        coefficient.append((a, b, c[i], d))
    return coefficient
def Spline(x_array,coefficient,num,x_val):
    for item in range(num):
        if x_array[item] <= x_val <= x_array[item + 1]:
            a_el, b_el, c_el, d_el = coefficient[item]
            diff_x = x_val - x_array[item]
            return a_el + b_el * diff_x + c_el * diff_x ** 2 + d_el * diff_x ** 3
    return None
num = int(input('Количество разбиений: '))
N=num+1
func = input('Функция: ')
x_array = np.linspace(-1, 1, num+1)
y_array = function(x_array, func)
c=GetMatrix(x_array,y_array,num,N)
coefficient=GetIndex(x_array,y_array, num, c)
x_spline = np.linspace(-1, 1, 100)
y_spline = [Spline(x_array,coefficient,num,x) for x in x_spline]
y_original = function(x_spline,func)
fig, ax = plt.subplots()
plt.plot(x_spline, y_spline, label='Кубический сплайн', color='black')
plt.scatter(x_array, y_array, color='red', label='Точки')
plt.plot(x_spline, y_original, label='Обыкновенная функция', color='green', linestyle='--')
ax.legend()
plt.grid()
plt.show()
