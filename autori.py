def _stdin():
    from sys import stdin
    for line in stdin:
        yield line

def autori():
    from sys import stdout
    from re import compile, sub
    line = _stdin()
    # Initial commentary

    regex = compile('[^A-Z]')
    stdout.write('%s\n' % regex.sub('', next(line).strip('\n')))

    return


if __name__ == '__main__':
    autori()
