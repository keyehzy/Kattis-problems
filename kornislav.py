def kornislav():
    a, b, c, d = sorted(map(int, input().split()), reverse=True)
    # two biggest in horizontal
    # choose the bigger
    # choose the lesser from the remaining
    print(min(a, b) * min(c, d))

    return


if __name__ == '__main__':
    kornislav()
