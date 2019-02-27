if __name__ == '__main__':
    e, f, c = map(int, input().split())
    total_empty = e + f
    drank = 0
    while total_empty >= c:
        total_empty -= c - 1
        drank += 1
    print(drank)
