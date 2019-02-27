def faktor():
    A, I = map(int, input().split())

    value = A / I
    while value == A / I:
        I -= 1

    return A * I + 1


if(__name__ == '__main__'):
    print(faktor())
