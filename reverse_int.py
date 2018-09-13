def reverse(x):
    """
    :type x: int
    """
    top = pow(2, 31) - 1
    base = -pow(2, 31)
    s = str(x)
    minus = False
    if s[0] == '-':
        s = s[1:]
        minus = True
    s = s[::-1]
    s.lstrip('0')
    if minus:
        s = '-' + s
    x = int(s)
    if x > top or x < base:
        return 0
    return x

"""
''.join(reverse(string))
string.lstrip()
"""
