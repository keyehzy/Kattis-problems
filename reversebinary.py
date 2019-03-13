def _stdin():
    from sys import stdin
    for line in stdin:
        yield line


def reversebinary():
    from sys import stdout
    line = _stdin()
    # Initial commentary

    n = str(bin(int(next(line))).strip('0b'))
    stdout.write('%d' % (int(n[::-1], 2)))
    return


if __name__ == '__main__':
    reversebinary()