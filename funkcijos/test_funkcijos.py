import unittest
import os, sys
# currentdir = os.path.dirname(os.path.realpath(__file__))
# parentdir = os.path.dirname(currentdir)
# sys.path.append(parentdir)
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
import funkcijos


class TestSkaiciu_suma(unittest.TestCase):
    def test_skaiciu_test(self):
        self.assertEqual(12, funkcijos.skaiciu_suma(3, 6, 3))

if __name__ == '__main__':
    unittest.main()