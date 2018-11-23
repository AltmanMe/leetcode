from basic.deque import Deque

def pal_checker(s):
    """
    s: string
    """
    
    char_deque = Deque()
    flag = True

    for char in s:
        char_deque.add_front(char)

    while char_deque.size() > 1 and flag:
        first = char_deque.remove_front()
        last = char_deque.remove_rear()
        if first != last:
            flag = False

    return flag

print(pal_checker("lsdkjfskf"))
print(pal_checker("radar"))
