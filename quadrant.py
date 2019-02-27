def quadrant():
    x, y = int(input()), int(input())
    if x > 0 and y > 0: return 1
    if x < 0 and y > 0: return 2
    if x < 0 and y < 0: return 3
    if x > 0 and y < 0: return 4


if __name__ == '__main__':
    print(quadrant())
