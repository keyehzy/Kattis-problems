def grassseed():
    c = float(input())
    l = int(input())

    sum = 0
    for _ in range(l):
        x, y = map(float, input().split())

        sum += x * y * c
    print(format(round(sum, 7), '.7f'))
    return


if __name__ == '__main__':
    grassseed()
