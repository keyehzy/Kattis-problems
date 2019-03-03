def symmetricorder():
    n = int(input())
    set = 1
    while True:
        s1, s2 = [], []
        print('SET ' + str(set))
        for j in range(n):
            if j % 2 == 0:
                print(input())
            else:
                s1.append(input())

        for s in reversed(s1):
            print(s)

        n = int(input())
        if n == 0:
            break
        else:
            set += 1
    return


if __name__ == '__main__':
    symmetricorder()
