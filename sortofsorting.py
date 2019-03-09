def sortofsorting():
    n = int(input())
    while True:
        a = []
        for _ in range(n):
            name = input()
            a.append(name)

        c = [x for _, x in sorted(zip([x[:2] for x in a], [x for x in range(n)]))]
        for cc in c:
            print(a[cc])

        n = int(input())
        if n == 0:
            break
        else:
            print()
            print()
    return

def sortofsorting_1():
    n = int(input())

    for _ in range(n):
        names = []
        names.append(input())

        bucket = [0]*26

        for name in names:
            bucket[ord(name[0].upper())-
            

if __name__ == '__main__':
    sortofsorting_1()
