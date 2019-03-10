def _stdin():
    from sys import stdin
    for line in stdin:
        yield line


def func(p, a, b, c, d, n):
    from math import sin, cos
    for k in range(1, n+1):
        yield p * (sin(a * k + b) + cos(c * k + d) + 2)


def artichoke():
    from sys import stdout
    line = _stdin()
    # Initial commentary

    p, a, b, c, d, n = map(int, next(line).split())

    it = func(p, a, b, c, d, n)

    try:
        diff = 0
        val = next(it)
        while True:
            n = next(it)
            if (val < n):
                val = n
            elif val - n > diff:
                diff = val - n
    except StopIteration:
        stdout.write("%.7lf\n" % diff)
        pass
    return


if __name__ == '__main__':
    artichoke()
