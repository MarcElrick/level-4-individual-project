import unittest
# Smoke test to verify test suite works
class SmokeTest(unittest.TestCase):

    def test_smoke(self):
        self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()