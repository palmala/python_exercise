import unittest
from sorting.in_place import bubble_sort
from sorting.in_place import quicksort
import logging
from hypothesis import given, strategies as some

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

SORTING_ALGOS = [quicksort]


class SortTests(unittest.TestCase):

    def test_simple_sort(self):
        a_list = [1, 5, 4, 2, 3]
        for sorting in SORTING_ALGOS:
            logging.debug(f"Checking {sorting}")
            subject = a_list.copy()
            sorting(subject)
            self.assertEqual([1, 2, 3, 4, 5], subject, f"Sorting failed for {sorting.__name__}!")

    @given(a_list=some.lists(some.integers(), min_size=10, max_size=50))
    def test_behavior(self, a_list):
        print(len(a_list))
        for sorting in SORTING_ALGOS:
            subject = a_list.copy()
            sorting(subject)
            self.assertEqual(len(a_list), len(subject), f"Sorting failed for {sorting.__name__}!")


if __name__ == "__main__":
    unittest.main()
