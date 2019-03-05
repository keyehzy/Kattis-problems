import math
def racingthealphabet():
    arc = 2.0 * math.pi * 30.0 / 28.0

    n = int(input())
    for _ in range(n):
        phrase = input().replace(' ', "[").replace(r"'", r"\\")
        total = 0
        for j in range(len(phrase)-1):
            q = abs(ord(phrase[j]) - ord(phrase[j+1]))
            forw = abs(ord(phrase[j]) - 92) + abs(ord(phrase[j+1]) - 64)
            back = abs(ord(phrase[j]) - 64) + abs(ord(phrase[j+1]) - 92) 
            total += min(q,forw,back) 

        print('%.10f' % (len(phrase) + total * arc / 15.0))
    return


if __name__ == '__main__':
    racingthealphabet()

