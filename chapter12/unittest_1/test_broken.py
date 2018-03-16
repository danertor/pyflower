import unittest
import sys
class SkipTests(unittest.TestCase):
    @unittest.expectedFailure
    def test_failes(self):
        self.assertEqual(False, True)

    @unittest.skip("Test is useless. Do not run")
    def test_skip(self):
        self.assertEqual(False, True)

    @unittest.skipIf(sys.version_info.minor == 6, "broken on 3.6")
    def test_skipif(self):
        self.assertEqual(False, True)

    @unittest.skipUnless(sys.platform.startswith('linux'), "broken unless on linux")
    def test_skipunless(self):
        self.assertEqual(False, True)

if __name__ == "__main__":
    print("Executing " + __name__)
    unittest.main()