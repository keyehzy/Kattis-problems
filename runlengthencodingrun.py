def _stdin():
    from sys import stdin
    for line in stdin:
        yield line
def encode(m):
    c = ''
    for i in range(len(m)):
        cnt = 1
        for j in range(i+1, len(m)):
            if m[j] == m[i]:
                cnt += 1
            else:
                break
        c += m[i] + str(cnt)
        i += cnt - 1
    return c
def decode(c):
    m = ''
    for i in range(len(c)):
        if c[i].isdigit():
            cnt = c[i] - '0'
            m += str(cnt - 1, c[i-1])
        else:
            m += c[i]
    return m

def runlengthencodingrun():
    from sys import stdout
    from collections import OrderedDict
    line = _stdin()
    # Initial commentary

    mode, inp = map(str, next(line).split())

    print(encode(inp))

    return


if __name__ == '__main__':
    runlengthencodingrun()