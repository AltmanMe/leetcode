from basic.stack import Stack

def to_str(n,base):
    lookup = '0123456789ABCDEF'
    if n < base:
        return lookup[n]
    else:
        return to_str(n//base,base) + lookup[n%base]

def to_str2(n,base):
    stack = Stack()
    lookup = '0123456789ABCDEF'
    while n:
        if n < base:
            stack.push(lookup[n])
        else:
            stack.push(lookup[n%base])
        n = n // base
    res = ''
    while not stack.isEmpty():
        res = res + stack.pop()
    return res


print(to_str(1453,16))
print(to_str2(10,2))
print(to_str(134344234332,2))
