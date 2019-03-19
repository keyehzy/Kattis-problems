from sys import stdin, stdout

input = iter(stdin.read().splitlines()).__next__


def write(x):
    return stdout.write(x)


def bossbattle():
    # Initial commentary
    n = int(input())
    if n < 4:
        write('%d' % 1)
        return
    pos = [0 for x in range(n)]
    bomb, pos[bomb] = 0, 1
    boss = bomb + 2
    j = 0
    while pos[boss] != 1:
        bomb = (bomb + 1) % n
        pos[bomb] = 1
        boss = (boss + 1) % n
        j += 1
    write('%d' % j)
    return


if __name__ == '__main__':
    bossbattle()
