def parking2():
    t = int(input())
    for _ in range(t):
        n = int(input())
        pos = sorted(list(map(int, input().split())))

        opt = int(round(sum(pos)/len(pos)))
         
        tot = abs(pos[0] - pos[-1]) + abs(opt - pos[0]) + abs(opt - pos[-1])
        print(tot)
        
    return


if __name__ == '__main__':
    parking2()

