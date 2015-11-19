#!/usr/bin/python3

import unittest
from harmonic import *

class HarmonicTest(unittest.TestCase):
    def testSum(self):
        harmonic = Harmonic()
        self.assertEqual(harmonic.sum(3,2), '1.5000000000000', "Deben ser iguales")

    def testSum(self):
        harmonic = Harmonic()
        self.assertEqual(harmonic.sum(3,3), '1.5000000000000', "Deben ser iguales")

    def testSum(self):
        harmonic = Harmonic()
        self.assertEqual(harmonic.sum(3,2), '1.5000000000000', "Deben ser iguales")
if __name__ == '__main__':
        unittest.main()
