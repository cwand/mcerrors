import unittest
import mcerrors
# import numpy as np


class TestPython(unittest.TestCase):

	def test_1plus2(self):
		self.assertEqual(mcerrors.f(2), 3)
