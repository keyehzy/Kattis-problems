from sys import stdin, stdout

input = iter(stdin.read().splitlines()).__next__


def write(x):
    return stdout.write(x)


def kemija():
    # Initial commentary

    s = list(input().split())
    r = ''
    for ss in s:
        ss = ss.replace('apa', 'a').replace('epe', 'e').replace('ipi', 'i').replace('opo', 'o').replace('upu', 'u')
        r += " "+ss
    print(r)
    return


if __name__ == '__main__':
    kemija()