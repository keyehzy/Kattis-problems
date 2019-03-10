def _stdin():
    from sys import stdin
    for line in stdin:
        yield line


def deathknight():
    from sys import stdout
    line = _stdin()
    # Initial commentary

    n = int(next(line))
    c = 0
    for _ in range(n):
        if next(line).strip('\n').find('CD') == -1:
            c += 1
    stdout.write(str(c))

    return


if __name__ == '__main__':
    deathknight()
