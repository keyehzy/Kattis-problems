def nastyhacks():
    n = int(input())
    
    for _ in range(n):
        r, e, c = map(int, input().split())

        print ('advertise' if e - c > r else ('does not matter' if e - c == r else 'do not advertise'))
    return

if __name__ == '__main__':
    nastyhacks()

