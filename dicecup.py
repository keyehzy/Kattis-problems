def dicecup():
    m, n = map(int, input().split())

    p = []
    q = [0]*(m+n)

    for i in range(m):
        for j in range(n):
            idx = i+j+2
            if idx in p:
                q[p.index(idx)] += 1
            else:
                p.append(idx)
                q[p.index(idx)] += 1

    q, p = zip(*sorted(zip(q, p)))
    max = q[-1]

    for i, q_ in enumerate(q):
        if q_ == max:
            print(p[i])
    return


if __name__ == '__main__':
    dicecup()
