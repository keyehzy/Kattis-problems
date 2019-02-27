def oddities():
    n = int(input())

    for _ in range(n):
        x = int(input())
        print(str(x) + ' is even' if x % 2 == 0 else str(x) + ' is odd')
    return


if __name__ == '__main__':
    oddities()
