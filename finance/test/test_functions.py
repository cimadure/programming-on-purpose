import numpy.testing as nt
import numpy as np
import unittest

from finance.functions import last_maximum_occurrence_index


class TestFunctions(unittest.TestCase):
    def test_something(self):
        nt.assert_array_equal([1.0, np.pi, np.nan], [1, np.pi, np.nan])

    def test_last_maximum_occurrence_with_1D_array(self):
        a = np.array([0, 0, 4, 4, 4, 4, 2, 2, 2, 2])
        self.assertEqual(5, last_maximum_occurrence_index(a))


if __name__ == '__main__':
    unittest.main()
