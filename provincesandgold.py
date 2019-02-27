def provincesandgold():
    hand = map(int, input().split())

    buypower = [3,2,1]
    hand_buypower = sum(p * q for p,q in zip(buypower, hand))
    
    dom = [[8,6], [5,3], [2,1]]
    dom_dict = {0:'Province', 1:'Duchy', 2:'Estate'}
    tre = [[6,3], [3,2], [0,1]]
    tre_dict = {0:'Gold', 1:'Silver', 2:'Copper'}

    word = ''

    for i, card in enumerate(dom):
        if card[0] <= hand_buypower:
            word += dom_dict[i]
            break
    
    if word:
        word += ' or '
    
    for  i, card in enumerate(tre):
        if card[0] <= hand_buypower:
            word += tre_dict[i]
            break
    print(word)
    return


if __name__ == '__main__':
    provincesandgold()

