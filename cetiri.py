from sys import stdin, stdout

input = iter(stdin.read().splitlines()).__next__


def write(x):
    return stdout.write(x)


def cetiri():
    # Initial commentary

    seq = list(sorted(map(int, input().split()))) + [0]

    m = 100
    for i in range(len(seq)-1):
        n = abs(seq[i+1] - seq[i])
        if n < m:
            m = n
    r = 0
    for i in range(len(seq)-1):
        n = seq[i+1] - seq[i]
        if n != m:
            r = seq[i] + m
            break
    write('%d' % r)
    return


if __name__ == '__main__':
    cetiri()
