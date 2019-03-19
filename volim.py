from sys import stdin, stdout

input = iter(stdin.read().splitlines()).__next__


def write(x):
    return stdout.write(x)


def volim():
    # Initial commentary

    k = int(input()) - 1
    n = int(input())

    time = 0
    for _ in range(n):
        nnn = input().split()
        lap, out = int(nnn[0]), nnn[1]
        if out == 'T':
            time += lap
            if time >= 210:
                break
            else:
                k = (k + 1) % 8
        else:
            time += lap
            if time >= 210:
                break
    print(k+1)

    return


if __name__ == '__main__':
    volim()