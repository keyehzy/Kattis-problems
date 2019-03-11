def _stdin():
    from sys import stdin
    for line in stdin:
        yield line


def cetvrta():
    from sys import stdout
    line = _stdin()
    # Initial commentary
    eps = 1337
    p1 = list(map(int, next(line).split()))
    p2 = list(map(int, next(line).split()))
    p3 = list(map(int, next(line).split()))

    p = [p1[0], p2[0], p3[0], p1[1]+eps, p2[1]+eps, p3[1]+eps]

    q = set()
    for pp in p:
        if pp in q:
            q.discard(pp)
        else:
            q.update({pp})

    x, y = min(list(q)), max(list(q))-1337
    stdout.write('%d %d' % (x, y))

    return


if __name__ == '__main__':
    cetvrta()
