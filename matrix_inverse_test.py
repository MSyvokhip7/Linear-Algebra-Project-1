import unittest
import Matrix

class TestMatrixInverse(unittest.TestCase):

    def test_LU_2x2_matrix(self):
        matrix = Matrix([3, 4], [5, 6])
        self.assertEqual(matrix.L.tolist(), [[1, 0], [0.6, 1]])
        self.assertEqual(matrix.U.tolist(), [[5, 6], [0, 0.4]])

    def test_LU_3x3_matrix(self):
        matrix = Matrix([[1, 2, 4], [2, 1, 2], [1, 2, 1]])
        self.assertEqual(matrix.L.tolist(), [[1, 0, 0], [0.5, 1, 0], [0.5, 1, 1]])
        self.assertEqual(matrix.U.tolist(), [[2, 1, 2], [0, 1.5, 0], [0, 0, 3]])

    def test_inverse_2x2_matrix(self):
        matrix = Matrix([[3, 4], [5, 6]])
        expected = [[-3, 2], [2.5, -1.5]]
        self.assertEqual(matrix.matrix_inverse().tolist(), expected)

    def test_inverse_3x3_matrix(self):
        matrix = Matrix([[1, 2, 4], [2, 1, 2], [1, 2, 1]])
        self.assertEqual(matrix.matrix_inverse().tolist(), [[0, -0.33, 0.66], [0.6, 0, -0.3], [-0.3, 0.3, 0]] )

    def test_not_square_matrix(self):
        matrix = Matrix([1, 2], [2, 3], [1, 2, 3])
        self.assertEqual(matrix.check_matrix(), "Wrong matrix")

    def test_det_matrix(self):
        pass

    def test_wrong_matrix(self):
        matrix  = Matrix([[1,2,3],[2, 3, 4], ["a", "b", "c"]])
        self.assertEquals(matrix.check_matrix(),"Wrong matrix")

if __name__ == '__main__':
    unittest.main()
