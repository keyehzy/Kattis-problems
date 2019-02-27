def spavanac():
    h, m = map(int, input().split())

    new_m = (m - 45) % 60
    if new_m > m:
        print((h-1) % 24, new_m)
    else:
        print(h, new_m)
    return


if __name__ == '__main__':
    spavanac()
