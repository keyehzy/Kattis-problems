def hydrashead():
    while True:
        h, t = map(int, input().split())
        if (h,t) == (0,0): break
        moves = 0
        while h>0 and t>0:
            gh, gt = 0, 0
            if t > 1:
                t -= 2
                gh += 1
            elif h > 1:
               h -= 2 
            else:
                t -= 1 
                gt += 2
            
            h += gh
            t += gt
            moves += 1
        print(moves)
    return

    
if __name__ == '__main__':
    hydrashead()
