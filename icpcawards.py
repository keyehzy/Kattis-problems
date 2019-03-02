def icpcawards():
    n = int(input())

    unis = []
    c = 0
    for _ in range(n):
        u, t = map(str, input().split())
        if u in unis or c > 11:
            continue
        else:
            unis.append(u)
            c += 1
            print(u + ' ' + t)

    return


if __name__ == '__main__':
    icpcawards()
