import unittest
from hypothesis import given, example, settings, reproduce_failure
import hypothesis.strategies as st


def is_even(v):
    return v % 2 == 0


class Test(unittest.TestCase):

    @given(st.integers())
    @settings(max_examples=100, print_blob=True)
    def test_is_even(self, x):
        res = is_even(x)
        print(x)
        self.assertEqual(res, (x % 2 == 0))


if __name__ == '__main__':
    unittest.main()
