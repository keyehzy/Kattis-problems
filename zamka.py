def zamka():
    l = int(input())
    d = int(input())
    x = int(input())

    idx = l
    j = 0
    while l <= abs(idx) <= d and j < 2:
        sum = 0
        n = abs(idx)
        while n:
            sum += n % 10
            n //= 10
        if sum == x:
            print(abs(idx))
            j += 1
            idx = -d-1
        idx += 1
    return


if __name__ == '__main__':
    zamka()
