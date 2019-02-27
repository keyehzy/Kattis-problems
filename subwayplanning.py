import math

def linearreg(x, y):
    n = len(x)

    b = 0
    xbar2 = 0

    for i in range(n):
        xbar2 += x[i]**2

    for i in range(n):
        b += x[i]*y[i] / xbar2

    return b


def distancetoline(x, y, b):
    n = len(x)
    result = [0]*n
    for i in range(n):
        result[i] = abs(-b * x[i] + y[i]) / math.sqrt(b**2 + 1)

    return result


def subwayplanning():
    #start with 1 group, see if conditions apply, if not split the group and repeat
    # we can start by doing some some linear regression
    # if conditions not apply split with k-mean and fit again

    n = int(input())

    for _ in range(n):
        num, d = map(int, input().split())

        condition = False

        x = [0]*num
        y = [0]*num

        for i in range(num):
            x[i], y[i] = map(int, input().split())

        b = linearreg(x, y)
        distance = distancetoline(x, y, b)
        condition = True

        x = [x for _, x in sorted(zip(distance, x))]
        y = [y for _, y in sorted(zip(distance, y))]






    return


if __name__ == '__main__':
    subwayplanning()
