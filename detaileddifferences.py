def detaileddifferences():
    n = int(input())

    for _ in range(n):
        s1 = input()
        s2 = input()

        re_s = ''
        l = len(s1)
        for i in range(l // 2):
            if s1[i] == s2[i]:
                re_s += '.'
            else:
                re_s += '*'
        print(s1)
        print(s2)
        print(re_s)
    return


if __name__ == '__main__':
    detaileddifferences()
