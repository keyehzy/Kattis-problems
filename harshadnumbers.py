def harshadnumbers():
    n = int(input())
    while True:
        m = n
        s = 0
        while m:
            s += m % 10
            m //= 10
        if n % s == 0:
            print(n)
            break
        n += 1
    return


if __name__ == '__main__':
    harshadnumbers()
