def seq_search(l, item):
    """
    l: list where search from
    item: search target
    """
    flag = False
    for i in l:
        if i == item:
            flag = True
            break

    return flag

def binary_search(l, item):
    """
    l must be sorted first
    """
    flag = False
    first = 0
    last = len(l) - 1
    while first <= last:
        mid = (first+last) // 2
        if l[mid] == item:
            flag = True
            break
        elif l[mid] < item:
            first = mid + 1
        else:
            last = mid - 1
    return flag

test_list1 = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(seq_search(test_list1, 3))
print(seq_search(test_list1, 13))

test_list2 = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binary_search(test_list2, 3))
print(binary_search(test_list2, 13))
