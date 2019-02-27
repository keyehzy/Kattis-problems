def cold():
    n = int(input())

    temp = list(map(int, input().split()))

    sum = 0
    for t in temp:
        if t < 0:
            sum += 1
    print(sum)
    return


if __name__ == '__main__':
    cold()
