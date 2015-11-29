#!/usr/bin/python3

import unittest
from harmonic import *

class HarmonicTest(unittest.TestCase):
    def testSum1(self):
        harmonic = Harmonic()
        self.assertEqual(harmonic.sum(3,2,1), [1,5,0], "Deben ser iguales")

    def testSum2(self):
        harmonic = Harmonic()
        self.assertEqual(harmonic.sum(1,1,1), [1], "Deben ser iguales")

    def testSum3(self):
        harmonic = Harmonic()
        self.assertEqual(harmonic.sum(10,3,1), [1,8,3,3,3,3,3,3,3,3], "Deben ser iguales")
if __name__ == '__main__':
        unittest.main()
