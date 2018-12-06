import numpy as np


def quick_sort(array, first, last):
    if first < last:
        split_point = partition(array, first, last)

        quick_sort(array, first, split_point-1)
        quick_sort(array, split_point+1, last)


def partition(array, first, last):
    pivot_value = array[first]

    left_mark = first + 1
    right_mark = last

    done = False
    while not done:

        while left_mark <= right_mark and array[left_mark] <= pivot_value:
            left_mark = left_mark + 1

        while right_mark >= left_mark and array[right_mark] >= pivot_value:
            right_mark = right_mark - 1

        if right_mark < left_mark:
            done = True
        else:
            tmp = array[left_mark]
            array[left_mark] = array[right_mark]
            array[right_mark] = tmp

    array[first], array[right_mark] = array[right_mark], array[first]

    return right_mark


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(alist, 0, len(alist)-1)
print(alist)
