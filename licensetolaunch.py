def _stdin():
    from sys import stdin
    for line in stdin:
        yield line
def licensetolaunch():
    from sys import stdout
    line = _stdin()
    n = int(next(line))

    days = list(map(int, next(line).split()))

    stdout.write(str(days.index(min(days))))
    return

if __name__ == '__main__':
    licensetolaunch()

