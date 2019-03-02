def judgingmoose():
    l, r = map(int, input().split())

    if l == 0 and r == 0:
        print('Not a moose')
    elif l == r:
        print('Even ' + str(2 * l))
    else:
        print('Odd ' + str(2 * max(l, r)))
    return


if __name__ == '__main__':
    judgingmoose()
