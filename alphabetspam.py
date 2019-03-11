def _stdin():
    from sys import stdin
    for line in stdin:
        yield line

def alphabetspam():
    from sys import stdout

    line = _stdin()
    # Initial commentary

    spam  = next(line).strip('\n')
    a, l = [0]*4, len(spam)

    for s in spam:
        if s == '_':
            a[0] += 1.0 / l
        elif s.islower():
            a[1] += 1.0 / l
        elif s.isupper():
            a[2] += 1.0 / l
        elif not s.isalpha():
            a[3] += 1.0 / l
    for n in a:
        stdout.write('%.16f\n' % (n))

    return


if __name__ == '__main__':
    alphabetspam()
