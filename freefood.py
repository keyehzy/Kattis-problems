def freefood():
    n = int(input())

    days = {}
    for _ in range(n):
        i, f = map(int,input().split())
        
        for j in range(i,f+1):
            days[j] = ''

    print(len(days))
    return

if __name__ == '__main__':
    freefood()

