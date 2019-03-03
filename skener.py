def skener():
    ny, nx, zy, zx = map(int, input().split())
    
    for __ in range(ny):
        row = input()
        s = ''
        for r in row:
            if zx > 0:
                for _ in range(zx):
                    s += r
        if zy > 0:
            for _ in range(zy):
                print(s)
    return

if __name__ == '__main__':
    skener()

