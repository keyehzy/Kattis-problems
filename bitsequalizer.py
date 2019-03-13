def _stdin():
    from sys import stdin
    for line in stdin:
        yield line


def distance(a, b):
    if not a:
        return len(b)
    if not b:
        return len(a)
    cost = 0 if a[0] == '0' and b[0] == '1' else 1 << 29
    return min(
        distance(a[1:], b[1:]) + cost,
        distance(a[2:], b[2:]) + 1)

def bitsequalizer():
    from sys import stdout
    line = _stdin()
    # Initial commentary

    # 101 -> 111
    a, b = '000', '110'

    print(distance(a, b))
    return

#    if i1 != i2:
#        if '?' in a:
#            #
#            pass
#        else:
#            print('-1')
#    else:
#        print(distance(a, b, len(a)-1, len(b)-1)



if __name__ == '__main__':
    bitsequalizer()