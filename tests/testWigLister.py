import unittest
from camap.csmap import WigLister


class WigListerTest(unittest.TestCase):

    def setUp(self):
        self.wig_lister = WigLister('scores.tar')

    def tearDown(self):
        self.wig_lister = None

    def test_t1(self):
        self.assertEqual(0.502, self.wig_lister.map('chrTest', 1, 3))

    def test_t2(self):
        self.assertEqual(0.421, self.wig_lister.map('chrTest', 2, 8))

    def test_t3(self):
        self.assertEqual(0.425, self.wig_lister.map('chrTest', 1, 10))

    def test_t4(self):
        self.assertEqual(0.425, self.wig_lister.map('chrTest', 1, 13))

    def test_t5(self):
        self.assertEqual(0.555, self.wig_lister.map('chrTest', 2, 13))

    def test_t6(self):
        self.assertEqual(0.509, self.wig_lister.map('chrTest', 19, 30))

    def test_t7(self):
        self.assertEqual(0.509, self.wig_lister.map('chrTest', 19, 35))

    def test_t8(self):
        self.assertEqual(0.564, self.wig_lister.map('chrTest', 18, 45))

    def test_t9(self):
        self.assertEqual(0.546, self.wig_lister.map('chrTest', 21, 50))

    def test_t10(self):
        self.assertEqual(0.639, self.wig_lister.map('chrTest', 24, 45))

    def test_t11(self):
        self.assertEqual(0.596, self.wig_lister.map('chrTest', 24, 50))

    def test_t12(self):
        self.assertEqual(0.596, self.wig_lister.map('chrTest', 24, 55))

    def test_t13(self):
        self.assertEqual(0.581, self.wig_lister.map('chrTest', 25, 66))

    def test_t14(self):
        self.assertEqual(0.557, self.wig_lister.map('chrTest', 18, 75))


if __name__ == '__main__':
    unittest.main()
