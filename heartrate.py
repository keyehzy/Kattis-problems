import math

def heartrate():
    n = int(input())
    for _ in range(n):

        b, p = map(float, input(). split())

        b1 = math.floor(p % b)
        b2 = abs(2*b - b1)

        print(format(round(60 * b1 / p, 4), '.4f'),
              format(round(60 * b / p, 4), '.4f'),
              format(round(60 * b2 / p, 4), '.4f'))
    return


if __name__ == '__main__':
    heartrate()
