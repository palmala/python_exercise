import unittest
from sorting.in_place import bubblesort
from sorting.in_place import quicksort
from hypothesis import settings, given, strategies as some

settings(max_examples=1)

SORTING_ALGOS = [bubblesort, quicksort]


class SortTests(unittest.TestCase):

    def test_simple_sort(self):
        a_list = [1, 5, 2, 4, 3]
        for sorting in SORTING_ALGOS:
            subject = a_list.copy()
            sorting(subject)
            self.assertEqual([1, 2, 3, 4, 5], subject, f"Sorting failed for {sorting.__name__}!")

    @given(a_list=some.lists(some.integers(min_value=0, max_value=10), min_size=10, max_size=50))
    @settings(max_examples=100)
    def test_behavior(self, a_list):
        for sorting in SORTING_ALGOS:
            subject = a_list.copy()
            sorting(subject)
            self.assertEqual(len(a_list), len(subject), f"Sorting failed for {sorting.__name__}!")
            self.assertTrue(all([subject[i] <= subject[i + 1] for i in range(len(subject) - 1) if len(subject) > 0]))


if __name__ == "__main__":
    unittest.main()
