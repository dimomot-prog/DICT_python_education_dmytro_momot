import sys


def read_matrix(prompt=""):
    if prompt:
        print(prompt)
    rows, cols = map(int, input("Введите размер матрицы (строки столбцы): ").split())
    print("Введите элементы матрицы построчно:")
    matrix = []
    for _ in range(rows):
        row = list(map(float, input().split()))
        matrix.append(row)
    return matrix, rows, cols


def print_matrix(matrix):
    print("Результат:")
    for row in matrix:
        print(*(f"{elem:g}" for elem in row))
    print()


def add_matrices():
    mat1, r1, c1 = read_matrix("Первая матрица:")
    mat2, r2, c2 = read_matrix("Вторая матрица:")

    if r1 != r2 or c1 != c2:
        print("Ошибка: матрицы должны быть одинакового размера!\n")
        return

    result = [[mat1[i][j] + mat2[i][j] for j in range(c1)] for i in range(r1)]
    print_matrix(result)


def multiply_by_constant():
    mat, rows, cols = read_matrix()
    const = float(input("Введите константу: "))
    result = [[mat[i][j] * const for j in range(cols)] for i in range(rows)]
    print_matrix(result)


def multiply_matrices():
    mat1, r1, c1 = read_matrix("Первая матрица:")
    mat2, r2, c2 = read_matrix("Вторая матрица:")

    if c1 != r2:
        print("Ошибка: количество столбцов первой матрицы должно совпадать с количеством строк второй!\n")
        return

    result = [[sum(mat1[i][k] * mat2[k][j] for k in range(c1)) for j in range(c2)] for i in range(r1)]
    print_matrix(result)


def transpose_matrix():
    print("\n1. Главная диагональ\n2. Побочная диагональ\n3. Вертикальная линия\n4. Горизонтальная линия")
    choice = input("Выберите тип транспонирования: ")
    mat, rows, cols = read_matrix()

    if choice == '1':
        result = [[mat[j][i] for j in range(rows)] for i in range(cols)]
    elif choice == '2':
        result = [[mat[rows - 1 - j][cols - 1 - i] for j in range(rows)] for i in range(cols)]
    elif choice == '3':
        result = [[mat[i][cols - 1 - j] for j in range(cols)] for i in range(rows)]
    elif choice == '4':
        result = [[mat[rows - 1 - i][j] for j in range(cols)] for i in range(rows)]
    else:
        print("Неверный выбор!\n")
        return

    print_matrix(result)


def get_determinant(mat):
    n = len(mat)
    if n == 1:
        return mat[0][0]
    if n == 2:
        return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]

    det = 0
    for col in range(n):
        sub_mat = [row[:col] + row[col + 1:] for row in mat[1:]]
        det += ((-1) ** col) * mat[0][col] * get_determinant(sub_mat)
    return det


def calculate_determinant():
    mat, rows, cols = read_matrix()
    if rows != cols:
        print("Ошибка: матрица должна быть квадратной!\n")
        return
    det = get_determinant(mat)
    print(f"Результат:\n{det:g}\n")


def inverse_matrix():
    mat, rows, cols = read_matrix()
    if rows != cols:
        print("Ошибка: матрица должна быть квадратной!\n")
        return

    det = get_determinant(mat)
    if det == 0:
        print("Ошибка: у этой матрицы нет обратной (определитель = 0).\n")
        return

    n = rows
    cofactors = []
    for r in range(n):
        cofactor_row = []
        for c in range(n):
            sub_mat = [row[:c] + row[c + 1:] for row in (mat[:r] + mat[r + 1:])]
            cofactor_row.append(((-1) ** (r + c)) * get_determinant(sub_mat))
        cofactors.append(cofactor_row)

    adjugate = [[cofactors[j][i] for j in range(n)] for i in range(n)]
    result = [[adjugate[i][j] / det for j in range(n)] for i in range(n)]
    print_matrix(result)


def main():
    while True:
        print("1. Сложить матрицы")
        print("2. Умножить матрицу на константу")
        print("3. Умножить матрицы")
        print("4. Транспонировать матрицу")
        print("5. Вычислить определитель")
        print("6. Обратная матрица")
        print("0. Выход")
        choice = input("Ваш выбор: ")

        if choice == '1':
            add_matrices()
        elif choice == '2':
            multiply_by_constant()
        elif choice == '3':
            multiply_matrices()
        elif choice == '4':
            transpose_matrix()
        elif choice == '5':
            calculate_determinant()
        elif choice == '6':
            inverse_matrix()
        elif choice == '0':
            break


if __name__ == "__main__":
    main()