import math


def bubble_sort(a_list):
    for i in range(len(a_list)):
        for j in range(i + 1, len(a_list)):
            if a_list[i] > a_list[j]:
                a_list[i], a_list[j] = a_list[j], a_list[i]


def _quicksort(a_list, lo, hi):
    if all([lo >= 0, hi >= 0, lo < hi]):
        pivot = _partition(a_list, lo, hi)
        _quicksort(a_list, lo, pivot)
        _quicksort(a_list, pivot + 1, hi)


def quicksort(a_list):
    _quicksort(a_list, 0, len(a_list) - 1)


def _partition(a_list, lo, hi):
    pivot = a_list[math.floor((lo + hi) / 2)]
    while True:
        while a_list[lo] < pivot:
            lo = lo + 1
        while a_list[hi] > pivot:
            hi = hi - 1
        if lo >= hi:
            return hi

        _swap(a_list, lo, hi)


def _swap(a_list, lo, hi):
    a_list[lo], a_list[hi] = a_list[hi], a_list[lo]