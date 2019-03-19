from sys import stdin, stdout

input = iter(stdin.read().splitlines()).__next__


def write(x):
    return stdout.write(x)


def tri():
    # Initial commentary

    a, b, c = map(int, input().split())
    if a + b == c:
        write("%d+%d=%d" % (a, b, c))
    elif a - b == c:
        write("%d-%d=%d" % (a, b, c))
    elif a * b == c:
        write("%d*%d=%d" % (a, b, c))
    elif a / b == c:
        write("%d/%d=%d" % (a, b, c))
    elif a == b + c:
        write("%d=%d+%d" % (a, b, c))
    elif a == b - c:
        write("%d=%d-%d" % (a, b, c))
    elif a == b * c:
        write("%d=%d*%d" % (a, b, c))
    elif a == b / c:
        write("%d=%d/%d" % (a, b, c))

    return


if __name__ == '__main__':
    tri()