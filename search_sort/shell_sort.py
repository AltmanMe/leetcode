import numpy as np


def shell_sort(array):
    sublist_num = len(array) // 2
    while sublist_num:
        for start in range(sublist_num):
            gap_insertion_sort(array, start, sublist_num)
        print('After increments of size {}. The array is {}'.format(
            sublist_num, array))
        sublist_num = sublist_num // 2


def gap_insertion_sort(array, start, gap):
    for i in range(start+gap, len(array), gap):
        cur_value = array[i]
        pos = i

        while pos >= gap and array[pos-gap] > cur_value:
            array[pos] = array[pos-gap]
            pos = pos - gap

        array[pos] = cur_value


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shell_sort(alist)
print(alist)
