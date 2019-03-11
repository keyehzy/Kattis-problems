def _stdin():
    from sys import stdin
    for line in stdin:
        yield line

def speedlimit():
    from sys import stdout
    line = _stdin()
    # Initial commentary
    while True:
        n = int(next(line))
        if n == -1:
            break
        last_s, last_t = map(int, next(line).split())
        m = last_s * last_t
        for _ in range(n-1):
            s, t = map(int, next(line).split())
            m += s * (t-last_t)
            last_t = t
        stdout.write('%d miles\n' % (m))
    return


if __name__ == '__main__':
    speedlimit()
