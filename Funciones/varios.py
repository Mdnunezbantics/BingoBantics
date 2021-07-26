def saca_x(c):
    pos = 0
    for digit in c:
        if digit == 'X':
            del c[pos]
        pos = pos + 1
    pos = 0
    for digit in c:
        if digit == 'X':
            del c[pos]
        pos = pos + 1
    for digit in c:
        if digit == 'X':
            del c[pos]
        pos = pos + 1
    return c
