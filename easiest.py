from sys import stdin, stdout

input = iter(stdin.read().splitlines()).__next__


def write(x):
    return stdout.write(x)

def sumofdigits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

def easiest():
    # Initial commentary

    while True:
        n = int(input())
        if n == 0: break
        dign = sumofdigits(n)
        chosen = 0
        j = 11
        while True:
            if sumofdigits(n*j) == dign:
                chosen = j
                break
            j += 1
        write('%d\n' % chosen)
    return


if __name__ == '__main__':
    easiest()