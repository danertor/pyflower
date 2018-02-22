import unittest

class TestAdd(unittest.TestCase):
    def add(self, a=0):
        self.sum += a

    def setUp(self):
        self.sum = 0

    def test_addpositive(self):
        self.add(2)
        self.assertEquals(self.sum, 2)
