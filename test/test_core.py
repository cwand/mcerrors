import unittest
import mcerrors
# import numpy as np


class TestDistVariable(unittest.TestCase):

    def test_sample_1(self):
        a = mcerrors.DistVariable([1.5])
        self.assertEqual(a.sample(), 1.5)

    def test_sample_2(self):
        a = mcerrors.DistVariable([1.4, 2.7])
        x = a.sample()
        self.assertTrue((x == 1.4) or (x == 2.7))
