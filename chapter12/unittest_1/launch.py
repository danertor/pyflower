<<<<<<< HEAD
import unittest

class CheckNumbers(unittest.TestCase):
    def test_int_float(self):
        self.assertEqual(1, 1.0)

    def test_str_float(self):
        self.assertEqual(1, "1")
"""
Passing explicit list to unittest.main will prevent IPython and Jupyter look at sys.argv. Passing exit=Fals will prevent unittest.main to shutdown the kernell process
"""
unittest.main()
=======
import unittest

class CheckNumbers(unittest.TestCase):
    def test_int_float(self):
        self.assertEqual(1, 1.0)

    def test_str_float(self):
        self.assertEqual(1, "1")
"""
Passing explicit list to unittest.main will prevent IPython and Jupyter look at sys.argv. Passing exit=Fals will prevent unittest.main to shutdown the kernell process
"""
unittest.main()
>>>>>>> b829bcb465b0e32104dbe492037b6da0f67e9948
