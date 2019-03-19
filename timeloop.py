from sys import stdin, stdout

input = iter(stdin.read().splitlines()).__next__


def write(x):
    return stdout.write(x)


def timeloop():
    # Initial commentary

    n = int(input())
    for i in range(n):
        write("%d %s\n" % (i+1, "Abracadabra"))
    return


if __name__ == '__main__':
    timeloop()