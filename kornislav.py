def _stdin():
    from sys import stdin
    for line in stdin:
        yield line
def kornislav():
    from sys import stdout
    line = _stdin()
    a, b, c, d = sorted(map(int, next(line).split()), reverse=True)
    # two biggest in horizontal
    # choose the bigger
    # choose the lesser from the remaining
    stdout.write(str(int(min(a, b) * min(c, d))))
    return


if __name__ == '__main__':
    kornislav()
