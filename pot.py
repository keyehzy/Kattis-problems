def pot():
    n = int(input())

    result = 0

    for _ in range(n):
        s = list(input())
        pow = int(s.pop(-1))
        result += int(''.join(s))**pow

    print(result)
    return


if __name__ == '__main__':
    pot()
