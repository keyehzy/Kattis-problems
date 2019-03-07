def compositions():
    n = 4
    a = [0 for i in range(n + 1)]
    k = 1
    a[1] = n
    while k != 0:
        x = a[k - 1] + 1
        y = a[k] - 1
        k -= 1
        while x <= y and y % 2 != 0 and y % 2 != 0:
            a[k] = x
            y -= x
            k += 1
        a[k] = x + y
        print(a[:k+1])
    return



if __name__ == '__main__':
    compositions()