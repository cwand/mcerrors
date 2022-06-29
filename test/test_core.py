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


def f(x):
    return 3 * x


class TestPropagator(unittest.TestCase):

    def test_simple_1var(self):
        a = mcerrors.DistVariable([1.5])
        p = mcerrors.Propagator(f)
        p.addDistVariable(a)
        s = p.propagate(samples=3)
        self.assertEqual(4.5, s[0])
        self.assertEqual(4.5, s[1])
        self.assertEqual(4.5, s[2])
