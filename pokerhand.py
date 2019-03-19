from sys import stdin, stdout

input = iter(stdin.read().splitlines()).__next__


def write(x):
    return stdout.write(x)


def pokerhand():
    from collections import defaultdict
    # Initial commentary

    h = list(input().split())
    d = defaultdict(int)
    for hh in h:
        d[hh[0]] += 1
    print(d[sorted(d, key=d.get, reverse=True)[0]])

    return


if __name__ == '__main__':
    pokerhand()