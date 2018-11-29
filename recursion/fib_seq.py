import time

def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib_ite(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

def fib_seq(n):
    """
    print first nth sequence number
    """
    output = []
    for i in range(1,n+1):
        if i in [1, 2]:
            output.append(1)
        else:
            result = output[i-1-1] + output[i-2-1] # list's idx start from 0
            output.append(result)
    return output

print(fib(5))
print(fib(20))
print(fib_ite(5))
print(fib_ite(20))

# test performance
fib_method = [fib, fib_ite]
for i in range(2):
    start = time.time()
    res = fib_method[i](35)
    end = time.time()
    print('{} Time Usage: {} Result: {}'.format(fib_method[i], start-end, res))
