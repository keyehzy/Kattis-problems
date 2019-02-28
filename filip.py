def filip():
    n1, n2 = map(list, input().split())

    temp = n1[0]
    n1[0] = n1[-1]
    n1[-1] = temp

    temp = n2[0]
    n2[0] = n2[-1]
    n2[-1] = temp

    print(''.join(max(n1, n2)))
    return


if __name__ == '__main__':
    filip()

