import unittest

def average(seq):
    return sum(seq) / len(seq)

class TestAverage(unittest.TestCase):
    def test_zero(self):
        self.assertRaises(ZeroDivisionError, average, [])
    """
    The context manager allows us to write the code the way we would normally write
    it (by calling functions or executing code directly), rather than having to wrap the
    function call in another function call.
    """
    def test_with_zero(self):
        with self.assertRaises(ZeroDivisionError):
            average([])

    if __name__ == "__main__":
        unittest.main()


