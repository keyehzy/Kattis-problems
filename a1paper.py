from sys import stdin, stdout

input = iter(stdin.read().splitlines()).__next__


def write(x):
    return stdout.write(x)

def a1paper():
    # Initial commentary

    #  An = 2 * An-1

    n = int(input()) - 1
    A = list(map(int, input().split()))

    ledge = 2 ** (-3/4.)
    sedge = 2 ** (-5/4.)

    cost = 0
    nl = 1
    enough = False

    for i in range(len(A)):
        cost += ledge * nl
        ledge, sedge = sedge, ledge
        sedge /= 2

        nl *= 2
        nl -= A[i]

        if nl <= 0:
            enough = True
            break
    if enough:
        write('%.13f' % cost)
    else:
        print('impossible')

    return


if __name__ == '__main__':
    a1paper()
