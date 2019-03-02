import math


def humancannonball2():
    n = int(input())
    tol = math.pow(10, -11)
    for _ in range(n):
        v, o, x1, h1, h2 = map(float, input().split())

        t1 = x1 / v / math.cos(math.radians(o))
        y = x1 * math.tan(math.radians(o)) - (0.5 * 9.81) * t1 * t1

        if h1 + 1 + tol < y < h2 - 1 - tol:
            print('Safe')
        else:
            print('Not Safe')
    return


if __name__ == '__main__':
    humancannonball2()
