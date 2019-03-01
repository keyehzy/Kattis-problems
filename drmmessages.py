def drmmessages():
    enc = [ord(c) + 65 for c in input()]

    val = sum(enc)

    p, half = [], len(enc)//2
    for j in range(half):
        q = ((enc[j] + val + enc[j+half]) % 26 + 65)
        p.append(chr(q))

    print(''.join(p))
    return


if __name__ == '__main__':
    drmmessages()

