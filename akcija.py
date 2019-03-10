def _stdin():
    from sys import stdin
    for line in stdin:
        yield line


def akcija():
    from sys import stdout
    line = _stdin()
    # Initial commentary

    n = int(next(line))
    tot = sorted([int(next(line)) for i in range(n)], reverse=True)

    s = 0
    j = 0
    while j < len(tot) - 2:
        s += tot[j] + tot[j+1]
        j += 3
    while j < len(tot):
        s += tot[j]
        j += 1

    stdout.write('%d\n' % (s))

    return


if __name__ == '__main__':
    akcija()
