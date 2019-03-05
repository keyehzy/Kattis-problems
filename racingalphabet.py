import math
def racingthealphabet():
    dx = 2.0 * math.pi * 30.0 / 27.0

    n = int(input())
    for _ in range(n):

        phrase = input().replace(' ', "[").replace("\'", "\\\\")
        
        total = 0
        for j in range(len(phrase)-1):
            q = abs(ord(phrase[j]) - ord(phrase[j+1]))
            qq = (65 + abs(ord(phrase[j]) + ord(phrase[j+1]))) % 28
            total += min(q,qq)
            print(total * dx / 15.0)
        
    return


if __name__ == '__main__':
    racingthealphabet()

