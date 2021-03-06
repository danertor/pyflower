<<<<<<< HEAD
from stats import StatsList
import unittest


class TestValidInputs(unittest.TestCase):
    # this is the method that gets called as setup
    def setUp(self):
        self.stats = StatsList([1, 2, 2, 3, 3, 4])

    def test_mean(self):
        self.assertEqual(self.stats.mean(), 2.5)

    def test_median(self):
        self.assertEqual(self.stats.median(), 2.5)
        self.stats.append(4)
        self.assertEqual(self.stats.median(), 3)

    def test_mode(self):
        self.assertEqual(self.stats.mode(), [2, 3])
        self.stats.remove(2)
        self.assertEqual(self.stats.mode(), [3])

    # gets called after each test case, to cleanup the mess and restore the previous state
    def tearDown(self):
        del self.stats
        self.stats = []
        self.assertListEqual(self.stats, [])


if __name__ == "__main__":
    unittest.main()
=======
from stats import StatsList
import unittest


class TestValidInputs(unittest.TestCase):
    # this is the method that gets called as setup
    def setUp(self):
        self.stats = StatsList([1, 2, 2, 3, 3, 4])

    def test_mean(self):
        self.assertEqual(self.stats.mean(), 2.5)

    def test_median(self):
        self.assertEqual(self.stats.median(), 2.5)
        self.stats.append(4)
        self.assertEqual(self.stats.median(), 3)

    def test_mode(self):
        self.assertEqual(self.stats.mode(), [2, 3])
        self.stats.remove(2)
        self.assertEqual(self.stats.mode(), [3])

    # gets called after each test case, to cleanup the mess and restore the previous state
    def tearDown(self):
        del self.stats
        self.stats = []
        self.assertListEqual(self.stats, [])


if __name__ == "__main__":
    unittest.main()
>>>>>>> b829bcb465b0e32104dbe492037b6da0f67e9948
