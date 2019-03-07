def sumsquareddigits():
    n = int(input())
    for _ in range(n):
        i, b, n = map(int, input().split())
        r = 0
        while n > 0:
            s = n % b
            n //= b
            r += s * s
        print(i, r)
    return


if __name__ == '__main__':
    sumsquareddigits()

