def _stdin():
    from sys import stdin
    for line in stdin:
        yield line


def aboveaverage():
    from sys import stdout
    line = _stdin()
    # Initial commentary

    n = int(next(line))

    for _ in range(n):
        cl = list(map(int, next(line).split()))
        nn = cl.pop(0)
        avg = sum([cl[x] for x in range(len(cl))]) / nn
        t = 0
        for c in sorted(cl):
            if c > avg:
                t += 100.0 / nn
        stdout.write("%.3f%s\n" % (t, '%'))
    return


if __name__ == '__main__':
    aboveaverage()