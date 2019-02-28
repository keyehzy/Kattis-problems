def bela():
    n, trump = map(str, input().split())

    trumped = {'A':11, 'K':4, 'Q':3, 'J':20, 'T':10, '9':14, '8':0, '7':0}

    not_trumped = trumped.copy()
    not_trumped['J'] = 2
    not_trumped['9'] = 0

    total = 0
    for _ in range(4*int(n)):
        card = input()
        value, suit = card[0], card[1]
        if suit == trump:
            total += trumped[value]
        else:
            total += not_trumped[value]
    print(total)
    return
            

if __name__ == '__main__':
    bela()

