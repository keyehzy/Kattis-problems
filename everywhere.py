def everywhere():
    t = int(input())

    for _ in range(t):
        n = int(input())
        c = {}
        for __ in range(n):
            city = input()
            c[city] = ' '
        print(len(c))
    return

if __name__ == '__main__':
    everywhere()

