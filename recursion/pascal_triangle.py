def pascal_tri(n):
    """
    n: integer number of rows
    """
    a = []
    for i in range(n):
        a.append([])
        a[i].append(1)
        for j in range(1,i):
            a[i].append(a[i-1][j-1]+a[i-1][j])
        if i:
            a[i].append(1)
    return a

tri1 = pascal_tri(6)
for line in tri1:
    print(line)
