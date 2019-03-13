def _stdin():
    from sys import stdin
    for line in stdin:
        yield line

def freefood():
    from sys import stdout
    line = _stdin()
    # Initial commentary

    n = int(next(line))

    days = set()
    for _ in range(n):
        i, f = map(int, next(line).split())
        for j in range(i, f+1):
            days.update({j})
    stdout.write('%d\n' % len(days))
    return


if __name__ == '__main__':
    freefood()
