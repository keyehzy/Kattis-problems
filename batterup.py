def batterup():
    n = int(input())

    bats = list(map(int, input().split()))

    result = 0.0

    for i in range(n):
        if bats[i] == -1:
            n -= 1
        else:
            result += bats[i]

    print(result / n)
    return


if __name__ == '__main__':
    batterup()
