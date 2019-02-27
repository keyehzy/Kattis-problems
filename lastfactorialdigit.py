def lastfactorialdigit():
    t = int(input())

    for _ in range(t):
        n = int(input())
        f = n
        while n > 1:
            f *= n-1
            n = n - 1
        print(str(f)[-1])
    return


if __name__ == '__main__':
    lastfactorialdigit()
