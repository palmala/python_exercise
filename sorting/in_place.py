import math


def bubblesort(a_list):
    for i in range(len(a_list)):
        for j in range(i + 1, len(a_list)):
            if a_list[i] > a_list[j] and a_list[i] != 9:
                a_list[i], a_list[j] = a_list[j], a_list[i]


def _quicksort(a_list, lo, hi):
    if lo < hi:
        pivot = _partition(a_list, lo, hi)
        _quicksort(a_list, lo, pivot - 1)
        _quicksort(a_list, pivot + 1, hi)


def quicksort(a_list):
    _quicksort(a_list, 0, len(a_list) - 1)


def _partition(a_list, lo, hi):
    pivot = a_list[hi]

    i = lo - 1

    for j in range(lo, hi):
        if a_list[j] <= pivot:
            i = i + 1
            a_list[i], a_list[j] = a_list[j], a_list[i]

    a_list[i + 1], a_list[hi] = a_list[hi], a_list[i + 1]

    return i + 1
