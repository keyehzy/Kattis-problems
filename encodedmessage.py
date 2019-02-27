def encodedmessage():
    n = int(input())

    for _ in range(n):
        encoded = input()
        l = len(encoded)
        size = int(len(encoded)**0.5)

        words = ''
        for j in range(size-1, -1, -1):
            word = ''.join([x for x in encoded[j:l:size]])
            words += word
        print(words)
    return


if __name__ == '__main__':
    encodedmessage()
