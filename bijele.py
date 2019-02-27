def bijele():
    pieces = list(map(int, input().split()))
    checker = [1, 1, 2, 2, 2, 8]

    return list(map(int.__sub__, checker, pieces))


if __name__ == '__main__':
    print(' '.join(map(str, bijele())))
