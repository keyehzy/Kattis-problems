def _stdin():
    from sys import stdin
    for line in stdin:
        yield line

def sortofsorting_2():
    from sys import stdin, stdout
    from operator import itemgetter

    line = _stdin()
    n = int(next(line))

    while True:
        a = []
        for _ in range(n):
            name = next(line)
            a.append(name)

        a.sort(key=itemgetter(0,1))
        for l in a:
            stdout.write(str(l))

        n = int(next(line)) 
        if n == 0:
            break
        else:
            stdout.write('\n')
            stdout.write('\n')
    return

if __name__ == '__main__':
    sortofsorting_2()

