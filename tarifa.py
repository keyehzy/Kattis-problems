def tarifa():

    x, n = int(input()), int(input())
    actual = x
    for j in range(n):
        actual -= int(input())
    return actual+n*x


if(__name__ == '__main__'):
    print(tarifa())
