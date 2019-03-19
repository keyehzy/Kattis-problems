from sys import stdin, stdout

input = iter(stdin.read().splitlines()).__next__


def write(x):
    return stdout.write(x)

def euclid(A, B):
    from math import sqrt, pow
    return sqrt(pow(A[0]-B[0], 2) + pow(A[1]-B[1], 2))

def distance(A, B, C):
    from math import sqrt
    AB = euclid(A, B)
    AC = euclid(A, C)
    BC = euclid(B, C)

    s = (AB + BC + AC) / 2.
    A = sqrt(s*(s-AB)*(s-AC)*(s-BC))
    return 2 * A / BC

def goatrope():
    # Initial commentary

    x, y, x1, y1, x2, y2 = map(int, input().split())

    A = (x, y)
    d = 0
    if x < x1:
        if y < y1:
            d = euclid(A, (x1, y1))
        elif y > y2:
            d = euclid(A, (x1, y2))
        else:
            d = distance(A, (x1, y1), (x1, y2))
    elif x > x2:
        if y < y1:
            d = euclid(A, (x2, y1))
        elif y > y2:
            d = euclid(A, (x2, y2))
        else:
            d = distance(A, (x2, y1), (x2, y2))
    else:
        if y < y1:
            d = distance(A, (x1, y1), (x2, y1))
        elif y > y2:
            d = distance(A, (x1, y2), (x2, y2))
    write('%f' % d)

    return


if __name__ == '__main__':
    goatrope()