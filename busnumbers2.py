def _stdin():
    from sys import stdin
    for line in stdin:
        yield line


def busnumbers2():
    from sys import stdout
    line = _stdin()
    # Initial commentary

    num = int(next(line))
    cubes = [x**3 for x in range(int(round(num**(4./11))))]

    sumof3 = {}
    for c1 in cubes:  # O(n)
        for c2 in cubes:  # O(n) -> O(n^2)
            if c1 + c2 <= num:
                if c1 + c2 in sumof3:
                    sumof3[c1+c2] += 1
                else:
                    sumof3[c1+c2] = 0
    for k in sorted(sumof3.keys(), reverse=True):
        if sumof3[k] > 2:
            stdout.write('%d\n' % k)
            return
    stdout.write('none\n')

    return


if __name__ == '__main__':
    busnumbers2()
