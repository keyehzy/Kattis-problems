from sys import stdin, stdout

input = iter(stdin.read().splitlines()).__next__


def write(x):
    return stdout.write(x)


def zanzibar():
    # Initial commentary

    n = int(input())

    for _ in range(n):
        a = list(map(int, input().split()))
        s = 0
        for j in range(len(a)-1):
            if a[j+1] > 2 * a[j]:
                s += a[j+1] - 2 * a[j]
        print(s)
    return


if __name__ == '__main__':
    zanzibar()