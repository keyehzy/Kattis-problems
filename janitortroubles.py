import math
def janitortroubles():
    # given that all inputs are quadrilatera
    sides = list(map(float, input().split()))

    s = sum(sides) / 2
    area = math.sqrt((s - sides[0]) * (s - sides[1]) * (s - sides[2]) * (s - sides[3]))

    print(area)
    return


if __name__ == '__main__':
   janitortroubles() 

