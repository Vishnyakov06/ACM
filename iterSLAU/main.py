import matplotlib.pyplot as plt
import numpy as np
def input_matrix():
    n = int(input("Введите количество строк (и столбцов) матрицы: "))
    A = np.zeros((n, n))
    print("Введите элементы матрицы:")
    for i in range(n):
        for j in range(n):
            A[i][j] = int(input(f"A[{i + 1}][{j + 1}]: "))
    return A
def input_vector(name, size):
    vector = np.zeros(size)
    print(f"Введите элементы вектора {name}:")
    for i in range(size):
        vector[i] = float(input(f"{name}[{i + 1}]: "))
    return vector
def isCorrect(matrix):
    for row in range(1,len(matrix)):
        if (matrix[row][row]==0):
            print("matrix is not correct")
            break
def jacobi_method(matrix,b,x0,eps,max_iter):
    n=len(matrix)
    x=x0
    norm=[]
    cnt=0
    for iteration in range(0,max_iter):
        x_new = [0] * n
        for i in range(0,n):
            _sum=0
            _sum=sum(matrix[i][j] * x[j] for j in range(n) if j != i)
            x_new[i]=(b[i]-_sum)/matrix[i][i]
        #квадратный корень из квадрата сумм
        norm_res=sum((x_new[i]-x[i])**2 for i in range (0,n))**0.5
        if norm_res < eps:
            print(f'Converged in iterations.')
            break
        norm.append(norm_res)
        cnt += 1
        x = x_new
    return cnt,x, norm
def zeyd_method(matrix,b,x0,eps,max_iter):
    n=len(matrix)
    x=x0
    norm=[]
    cnt=0
    for iteration in range(0,max_iter):
        x_new=x.copy()
        for i in range(0,n):
            _sum=0
            _sum=sum(matrix[i][j] * x[j] for j in range(n) if j != i)
            x[i]=(b[i]-_sum)/matrix[i][i]
        #квадратный корень из квадрата сумм
        norm_res=sum((x[i]-x_new[i])**2 for i in range (0,n))**0.5
        if norm_res < eps:
            print(f'Converged in iterations.')
            break
        norm.append(norm_res)
        cnt += 1
    return cnt,x, norm
def main():
    print("Ввведите количество итераций:")
    max_iter=int(input())
    print("Введите точность:")
    eps=float(input())
    A = input_matrix()
    n = A.shape[0]
    b = input_vector('b', n)
    initial_guesses = input_vector('начальный вектор', n)
    n,solution, norm_history = jacobi_method(A, b, initial_guesses,eps,max_iter)
    #n, solution, norm_history = zeyd_method(A, b, initial_guesses, eps, max_iter)
    print(solution)
    plt.plot(range(n), [norm_history[i] for i in range(0,n)],label=f'')
    plt.yscale('log')
    plt.xlabel('Количество итераций')
    plt.ylabel('Значение нормы')
    plt.title('Метод Якоби')
    plt.grid()
    plt.show()
if __name__ == "__main__":
    main()
