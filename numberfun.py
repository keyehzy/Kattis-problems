def numberfun():
    n = int(input())

    for _ in range(n):
        a, b, c = map(float, input().split())
        if a * b == c:
            print('Possible')
        elif a / b == c or b / a == c:
            print('Possible')
        elif c == a + b or c == a - b or c == b - a:
            print('Possible')
        else:
            print('Impossible')
    return


if __name__ == '__main__':
    numberfun()
