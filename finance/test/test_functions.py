import numpy.testing as nt
import numpy as np
import unittest

from finance.functions import last_maximum_occurrence_index, rescale, rescale_by_part


class TestMaximal(unittest.TestCase):

    def test_last_maximum_occurrence_with_1D_array(self):
        a = np.array([0, 0, 4, 4, 4, 4, 2, 2, 2, 2])
        self.assertEqual(5, last_maximum_occurrence_index(a))


class TestRescalingByPart(unittest.TestCase):

    def test_rescale_by_part_maximum(self):
        r = rescale_by_part(x=2., first=1., minimum=0.7, maximum=2.)
        self.assertEqual(1, r)

    def test_rescale_by_part_above(self):
        r = rescale_by_part(x=2, first=1.0, minimum=0.7, maximum=4.0)
        self.assertAlmostEqual(1./3, r)

    def test_rescale_by_part_idem(self):
        r = rescale_by_part(x=1.0, first=1.0, minimum=0.7, maximum=4.0)
        self.assertAlmostEqual(0., r)

    def test_rescale_by_part_minimum(self):
        r = rescale_by_part(x=0.7, first=1.0, minimum=0.7, maximum=4.0)
        self.assertAlmostEqual(-1., r)

    def test_rescale_by_part_bellow_assertion(self):
        with self.assertRaises(AssertionError) as context:
            rescale_by_part(x=0.5, first=1.0, minimum=0.7, maximum=4.0)

    def test_rescale_by_part_bellow(self):
        r = rescale_by_part(x=0.7, first=1.0, minimum=0.5, maximum=4.0)
        self.assertAlmostEqual(-0.6, r)

    def test_rescale_by_part_maximal_assertion(self):
        with self.assertRaises(AssertionError) as context:
            rescale_by_part(x=4.5, first=1.0, minimum=0.5, maximum=4.0)


class TestRescale(unittest.TestCase):

    def test_rescale(self):
        nt.assert_almost_equal(np.array([0, -1, 0.5, 1]), rescale(np.array([2, 1, 3, 4])))


if __name__ == '__main__':
    unittest.main()
