def cetvrta():
    x1, x2, x3 = list(map(int, input().split())), list(map(int, input().split())), list(map(int, input().split()))

    x = [x1, x2, x3]

    for i in range(2):
        y = list(map(int.__sub__, x[i+1], x[i]))
        if y[0] != 0:
            if y[0] > 0:
                return [x[(i + 2 % 1) - 1][0] - y[1], x[(i + 2 % 1)-1][1] + y[0]]
            else:
                return [x[(i + 2 % 1) - 1][0] - y[0], x[(i + 2 % 1)-1][1] + y[1]]
    return


if __name__ == '__main__':
    print(' '.join(map(str, cetvrta())))
