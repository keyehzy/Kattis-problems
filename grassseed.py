def _stdin():
    from sys import stdin
    for line in stdin:
        yield line


def grassseed():
    from sys import stdout
    line = _stdin()
    # Initial commentary

    c, l = float(next(line)), int(next(line))

    s = 0
    for _ in range(l):
        x, y = map(float, next(line).split())
        s += x * y * c
    stdout.write('%.7f' % s)

    return


if __name__ == '__main__':
    grassseed()
