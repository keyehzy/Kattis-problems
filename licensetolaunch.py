def licensetolaunch():
    n = int(input())

    days = list(map(int, input().split()))

    print(days.index(min(days)))
    return

if __name__ == '__main__':
    licensetolaunch()

