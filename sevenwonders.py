def sevenwonders():
    cards = input()

    count = [0]*3
    s = 0
    for c in cards:
        if c == 'T':
            count[0] += 1
        elif c == 'C':
            count[1] += 1
        elif c == 'G':
            count[2] += 1
    s = sum([x*x for x in count])

    ss = 0
    p = [1, 1, 1]
    while True:
        if all(x > 0 for x in count):
            count = [x - y for x, y in zip(count, p)]
            ss += 1
        else:
            break
    print(s + 7*ss)
    return


if __name__ == '__main__':
    sevenwonders()
