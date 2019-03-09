def sortofsorting_2():
    n = int(input())
    while True:
        a = []
        for _ in range(n):
            name = input()
            a.append(name)

        list1 = sorted(a, key= operator.itemgetter(0,1))
        for l in list1:
            print(l)

        n = int(input())
        if n == 0:
            break
        else:
            print()
            print()
    return

if __name__ == '__main__':
    sortofsorting_2()

