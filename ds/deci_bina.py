def base_converter(n,base):
    """
    n: decimal number
    base: convert decimal into base(2, 8, 16)
    """
    result = list()

    c = 0
    digits = '0123456789ABCDEF'

    if not n:
        return 0

    while n>0:
        c = n % base
        n = n // base
        result.append(digits[c])

    result = result[::-1]
    
    return ''.join(result)

print(base_converter(25,2))
print(base_converter(25,16))
