def _stdin():
    from sys import stdin
    for line in stdin:
        yield line

def doorman():
    from sys import stdout
    line = _stdin()
    # Initial commentary

    n = int(next(line))
    s = list(next(line).strip('\n'))

    m, w = 0, 0
    j = 0
    
    while j < len(s):
        k = s[j]
        if k == 'M':
            if m - w == n:
                if j < len(s) - 1 and s[j+1] == 'M':
                    break
                else:
                    m += 1
            else:
                m += 1
        if k == 'W':
            if w - m == n:
                if j < len(s) - 1 and s[j+1] == 'W':
                    break
                else:
                    w += 1
            else:
                w += 1
        j += 1
    stdout.write('%d\n' % j)

    return


if __name__ == '__main__':
    doorman()
