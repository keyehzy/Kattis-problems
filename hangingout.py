from sys import stdin, stdout

input = iter(stdin.read().splitlines()).__next__


def write(x):
    return stdout.write(x)


def handingout():
    # Initial commentary

    limit, e = map(int, input().split())
    curr = 0
    rej = 0
    for _ in range(e):
        ss = input().split()
        ee, next = ss[0], int(ss[1])
        if ee == "enter":
            if next + curr <= limit:
                curr += next
            else:
                rej += 1
        if ee == "leave":
            if curr > 0:
                curr -= next
    print(rej)

    return


if __name__ == '__main__':
    handingout()