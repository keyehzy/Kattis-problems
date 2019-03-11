def _stdin():
    from sys import stdin
    for line in stdin:
        yield line


def solve(h, t, move=0):
    from sys import stdout
    if h > 0 or t > 0:
        if t > 1:
            solve(h+1, t-2, move+1)
        elif h > 1:
            solve(h-2, t, move+1)
        else:
            solve(h, t+1, move+1)
    else:
        stdout.write('%d\n' % move)
        return


def hydrashead():
    line = _stdin()
    # Initial commentary

    while True:
        h, t = map(int, next(line).split())
        if (h, t) == (0, 0):
            break
        solve(h, t)
    return


if __name__ == '__main__':
    hydrashead()
