def planina():
    j = int(input())
    x = 2
    while(j):
        x += x - 1
        j -= 1
    print(x*x)
    return

if __name__ == '__main__':
    planina()

