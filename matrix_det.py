"""Модуль для вычисления определителя матрицы N x N из файла."""

import sys

def read_matrix(filepath):
    """Считывает размерность N и элементы матрицы из текстового файла."""
    with open(filepath, "r", encoding="utf-8") as f:
        tokens = f.read().split()

    if not tokens:
        return []

    n = int(tokens[0])
    matrix = []
    pos = 1
    for _ in range(n):
        row = [float(tokens[pos + i]) for i in range(n)]
        matrix.append(row)
        pos += n

    return matrix

def calculate_determinant(matrix):
    """Вычисляет определитель квадратной матрицы методом Гаусса."""
    n = len(matrix)
    if n == 0:
        return 0
    if n == 1:
        return matrix[0][0]

    # Копируем матрицу, чтобы не менять входные данные
    a = [row[:] for row in matrix]
    det = 1.0

    for i in range(n):
        # Поиск ведущего элемента по столбцу для численной устойчивости
        pivot = i
        for row in range(i + 1, n):
            if abs(a[row][i]) > abs(a[pivot][i]):
                pivot = row

        # Если ведущий элемент нулевой, определитель равен нулю
        if abs(a[pivot][i]) < 1e-12:
            return 0

        # Перестановка строк с учетом изменения знака определителя
        if pivot != i:
            a[i], a[pivot] = a[pivot], a[i]
            det = -det

        det *= a[i][i]

        # Обнуление элементов под главной диагональю
        for j in range(i + 1, n):
            factor = a[j][i] / a[i][i]
            for k in range(i, n):
                a[j][k] -= factor * a[i][k]

    # Приведение результата к целому числу, если погрешность минимальна
    if abs(det - round(det)) < 1e-9:
        return int(round(det))
    return round(det, 6)

def main():
    """Точка входа: чтение аргумента пути к файлу и вывод определителя."""
    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    matrix = read_matrix(filename)
    result = calculate_determinant(matrix)
    print(result)

if __name__ == "__main__":
    main()