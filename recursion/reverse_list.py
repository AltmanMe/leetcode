def reverse(l):
    """
    l: list type data
    """
    return [l[-1]] + reverse(l[:-1]) if l else []

l1 = list(range(6))
l2 = list(range(0,20,2))
print(reverse(l1))
print(reverse(l2))
