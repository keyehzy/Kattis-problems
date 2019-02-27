def fantriangulation(points):
    p0 = points[0]
    points.pop(0)
        
    areas = 0
    while(len(points) > 1):
        p1 = points[0]
        points.pop(0)
        p2 = points[0]
        
        #v1 = [p0[k]-p1[k] for k in range(len(p0))]
        #v2 = [p0[k]-p2[k] for k in range(len(p0))]
        v1 = tuple(map(lambda x,y: x-y, p0, p1))
        v2 = tuple(map(lambda x,y: x-y, p0, p2))
        
        cross = v1[0]*v2[1] - v1[1]*v2[0]
        areas += cross/2.0
    return areas

def convexpolygonarea():
    n = int(input())
    
    for nn in range(n):
        line = list(map(int, input().split()))        
        m = line[0]
        line.pop(0) # useless
        
        xy = list(zip(*[iter(line)]*2))
        result = fantriangulation(xy)
        
        if(result.is_integer()):
            print(round(result))
        else:
            print(result)
convexpolygonarea()
input()