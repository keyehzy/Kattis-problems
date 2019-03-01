from collections import Counter
def busnumbers2():
    num = int(input())
    cubes = [x**3 for x in range(int(round(num**(2./3))))]
     
    sumof3 = [] 
    for c1 in cubes:
        for c2 in cubes:
            if c1 + c2 <= num:
                sumof3.append(c1 + c2)
    count = Counter(sumof3)
    a = sorted(count.items(), reverse=True)
    number, occur = map(int, a[0])
    if occur//2 >=2:
        print(number)
    else:
        print('none')
    return
    

if __name__ == '__main__':
    busnumbers2()

