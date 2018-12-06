import numpy as np


def merge_sort(array):
    print('Splitting {}'.format(array))
    if len(array) > 1:
        mid = len(array) // 2
        left_ary = array[:mid]
        right_ary = array[mid:]

        merge_sort(left_ary)
        merge_sort(right_ary)

        i = 0  # left array index
        j = 0  # right array index
        k = 0  # merged array index

        while i < len(left_ary) and j < len(right_ary):
            if left_ary[i] < right_ary[j]:
                array[k] = left_ary[i]
                i = i + 1
            else:
                array[k] = right_ary[j]
                j = j + 1
            k = k + 1

        while i < len(left_ary):
            array[k] = left_ary[i]
            i = i + 1
            k = k + 1

        while j < len(right_ary):
            array[k] = right_ary[j]
            j = j + 1
            k = k + 1

    print('Merging {}'.format(array))


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
merge_sort(alist)
print(alist)
