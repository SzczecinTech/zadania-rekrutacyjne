def silnia(x):

    if ( x > 1 ):
        return x * silnia(x-1)
    elif ( x < 0 ):
        raise ValueError('Won')
    else:
        return 1

print(silnia(5))
