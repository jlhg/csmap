import unittest
from ..csmap import WigLister

expected = [
    [0.39, 0.257, 0.86],
    [0.257, 0.86, 0.896, 0.213, 0.235, 0.452, 0.034],
    [0.39, 0.257, 0.86, 0.896, 0.213, 0.235, 0.452, 0.034, 0.05, 0.866],
    [0.39, 0.257, 0.86, 0.896, 0.213, 0.235, 0.452, 0.034, 0.05, 0.866],
    [0.257, 0.860, 0.896, 0.213, 0.235, 0.452, 0.034, 0.050, 0.866],
    [0.096, 0.227, 0.459, 0.296, 0.035, 0.98, 0.497, 0.96, 0.888, 0.656],
    [0.096, 0.227, 0.459, 0.296, 0.035, 0.98, 0.497, 0.96, 0.888, 0.656],
    [0.096, 0.227, 0.459, 0.296, 0.035, 0.98, 0.497, 0.96, 0.888, 0.656, 0.499, 0.715, 0.364, 0.822, 0.962],
    [0.096, 0.227, 0.459, 0.296, 0.035, 0.98, 0.497, 0.96, 0.888, 0.656, 0.499, 0.715, 0.364, 0.822, 0.962, 0.029, 0.833, 0.511, 0.802, 0.291],
    [0.296, 0.035, 0.98, 0.497, 0.96, 0.888, 0.656, 0.499, 0.715, 0.364, 0.822, 0.962],
    [0.296, 0.035, 0.98, 0.497, 0.96, 0.888, 0.656, 0.499, 0.715, 0.364, 0.822, 0.962, 0.029, 0.833, 0.511, 0.802, 0.291],
    [0.296, 0.035, 0.98, 0.497, 0.96, 0.888, 0.656, 0.499, 0.715, 0.364, 0.822, 0.962, 0.029, 0.833, 0.511, 0.802, 0.291],
    [0.035, 0.98, 0.497, 0.96, 0.888, 0.656, 0.499, 0.715, 0.364, 0.822, 0.962, 0.029, 0.833, 0.511, 0.802, 0.291, 0.947, 0.351, 0.626, 0.385, 0.342, 0.295],
    [0.096, 0.227, 0.459, 0.296, 0.035, 0.98, 0.497, 0.96, 0.888, 0.656, 0.499, 0.715, 0.364, 0.822, 0.962, 0.029, 0.833, 0.511, 0.802, 0.291, 0.947, 0.351, 0.626, 0.385, 0.342, 0.295, 0.723, 0.538, 0.804, 0.781],
]


class WigListerTest(unittest.TestCase):

    def setUp(self):
        self.wig_lister = WigLister('tests/score.tar')

    def tearDown(self):
        self.wig_lister = None

    def test_t01(self):
        self.assertEqual(expected[0], self.wig_lister.map('chrTest', 1, 3, True))

    def test_t02(self):
        self.assertEqual(expected[1], self.wig_lister.map('chrTest', 2, 8, True))

    def test_t03(self):
        self.assertEqual(expected[2], self.wig_lister.map('chrTest', 1, 10, True))

    def test_t04(self):
        self.assertEqual(expected[3], self.wig_lister.map('chrTest', 1, 13, True))

    def test_t05(self):
        self.assertEqual(expected[4], self.wig_lister.map('chrTest', 2, 13, True))

    def test_t06(self):
        self.assertEqual(expected[5], self.wig_lister.map('chrTest', 19, 30, True))

    def test_t07(self):
        self.assertEqual(expected[6], self.wig_lister.map('chrTest', 19, 35, True))

    def test_t08(self):
        self.assertEqual(expected[7], self.wig_lister.map('chrTest', 18, 45, True))

    def test_t09(self):
        self.assertEqual(expected[8], self.wig_lister.map('chrTest', 21, 50, True))

    def test_t10(self):
        self.assertEqual(expected[9], self.wig_lister.map('chrTest', 24, 45, True))

    def test_t11(self):
        self.assertEqual(expected[10], self.wig_lister.map('chrTest', 24, 50, True))

    def test_t12(self):
        self.assertEqual(expected[11], self.wig_lister.map('chrTest', 24, 55, True))

    def test_t13(self):
        self.assertEqual(expected[12], self.wig_lister.map('chrTest', 25, 66, True))

    def test_t14(self):
        self.assertEqual(expected[13], self.wig_lister.map('chrTest', 18, 75, True))


if __name__ == '__main__':
    unittest.main()
