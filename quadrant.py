def _stdin():
    from sys import stdin
    for line in stdin:
        yield line


def quadrant():
    from sys import stdout
    line = _stdin()
    # Initial commentary

    x, y = int(next(line)), int(next(line))
    if x > 0 and y > 0:
        stdout.write('%d' % 1)
        return
    if x < 0 and y > 0:
        stdout.write('%d' % 2)
        return
    if x < 0 and y < 0:
        stdout.write('%d' % 3)
        return
    if x > 0 and y < 0:
        stdout.write('%d' % 4)
        return


if __name__ == '__main__':
    quadrant()
