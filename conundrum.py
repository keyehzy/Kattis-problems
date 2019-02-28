def conundrum():
    cipher = input()

    s = 'PER'
    days = 0
    for i, c in enumerate(cipher):
        if s[i % 3] == c:
            continue
        else:
            days += 1
    print(days)
    return


if __name__ == '__main__':
    conundrum()

