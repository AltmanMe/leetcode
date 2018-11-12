import numpy as np

def edit_distance(s1, s2):
    m = len(s1) + 1 # source string
    n = len(s2) + 1 # target string
    print('m: {}, n: {}'.format(m, n))
    distance = [[0] * m for _ in range(n)] # distance[i][j]: i from 0 to n-1, j from 0 to m-1
#    t = np.array(distance)
#    print('distance shape: {}'.format(t.shape))

    for i in range(n):
        distance[i][0] = i

    for j in range(m):
        distance[0][j] = j

    for i, c1 in enumerate(s2, start=1):
        for j, c2 in enumerate(s1, start=1):
#            print('i: {}, j: {}, c1: {}, c2: {}'.format(i, j, c1, c2))
            if c1 == c2:
                distance[i][j] = distance[i-1][j-1]
            else:
                distance[i][j] = min(distance[i-1][j] + 1, distance[i][j-1] + 1, distance[i-1][j-1] + 1)

    return distance[n-1][m-1]

def improved_(s1, s2):
    """
    two arraies: distance distance_, each length is len(shorter string)
    distance: previous row
    distance_: current row
    """

    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distance = range(len(s1) + 1)

    # i2: row, i1: col
    for i2, c2 in enumerate(s2, start=1):
        distance_ = [i2]
        for i1, c1 in enumerate(s1, start=1):
            if c1 == c2:
                distance_.append(distance[i1-1])
            else:
                distance_.append(1 + min(distance[i1-1], distance[i1], distance_[-1]))
        distance = distance_

    return distance[-1]
                                

s1 = 'a'
s2 = 'abcdef'
print(edit_distance(s1, s2))
print(improved_(s1, s2))
