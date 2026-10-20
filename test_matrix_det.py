"""Тестирование функции вычисления определителя матрицы."""

import unittest
from matrix_det import calculate_determinant

class TestMatrixDeterminant(unittest.TestCase):
    """Набор тестов для различных типов квадратных матриц."""

    def test_single_element(self):
        """Матрица 1x1."""
        self.assertEqual(calculate_determinant([[7]]), 7)

    def test_2x2_matrix(self):
        """Базовая матрица 2x2."""
        matrix = [[1, 2], [3, 4]]
        self.assertEqual(calculate_determinant(matrix), -2)

    def test_zero_determinant(self):
        """Матрица с линейно зависимыми строками (определитель 0)."""
        matrix = [[1, 2, 3], [4, 5, 6], [2, 4, 6]]
        self.assertEqual(calculate_determinant(matrix), 0)

    def test_identity_matrix(self):
        """Единичная матрица 3x3."""
        matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        self.assertEqual(calculate_determinant(matrix), 1)

    def test_pivot_zero_on_diagonal(self):
        """Матрица с нулем на диагонали, требующая перестановки строк."""
        matrix = [[0, 3], [2, 1]]
        self.assertEqual(calculate_determinant(matrix), -6)

    if __name__ == "__main__":
        unittest.main()