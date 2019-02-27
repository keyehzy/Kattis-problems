def qaly():
    n = int(input())
    sum = 0
    for _ in range(n):
        q, y = map(float, input().split())
        sum += q * y
    print(format(sum, '.3f'))
    return


if __name__ == '__main__':
    qaly()
