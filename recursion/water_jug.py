def water_jug(tup):
    """
    tup: tuple (x,y) 
    where x: the amount of water in the 4-gallon jug
          y: the amount of water in the 3-gallon jug
    initial state: (0,0)
    """
    if tup[0] == 2:
        return True
    x, y = tup
    # Full 4-gal jug
    if x < 4:
        return water_jug(4,y)
