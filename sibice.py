import math


def sibice():
    N, W, H = map(int, input().split())
    for j in range(N):
        size = int(input())
        if size <= W or size <= H or size <= math.sqrt(W**2 + H**2):
            print('DA')
        else:
            print('NE')
    return


if __name__ == '__main__':
    sibice()
