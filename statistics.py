def _stdin():
    from sys import stdin
    for line in stdin:
        yield line


def statistics():
    from sys import stdout
    line = _stdin()
    try:
        idx = 1
        while True:
            _line = list(map(int, next(line).split()))
            n, _min = _line[0], _line[1]
            _max = _min
            for j in range(2, n+1):
                m = _line[j]
                if m < _min:
                    _min = m
                if m > _max:
                    _max = m
            stdout.write('Case %d: %d %d %d\n' % (idx, _min,
                                                  _max, _max - _min))
            idx += 1
    except StopIteration:
        pass

    return


if __name__ == '__main__':
    statistics()
