#! /usr/bin/python3
def twostones():
    n = int(input())
    #Alice&Bob plays
    if((n - 4) % 2 == 0):
        print('Bob')
    else:
        print('Alice')

def aaah():
    s1 = str(input())
    s2 = str(input())

    if(len(s1) >= len(s2)):
        print('go')
    else:
        print('no')

def abandonedanimal():
    n_super = int(input())
    k = int(input())
    shop_items = {}
    
    for i in range(k):
        shop_item = str(input()).split()
        shop_items.append(shop_item)

    m = int(input())
    items = [] 
    for i in range(m):
        items.append(str(input()))
    
    isUnique = False
    isPossible = True    
    while(True):        
        for bought_item in items:
            shop_num = shop_items[0][0]
            for item in shop_items:
                if(bought_item == item[1] and item[0] >= shop_num):
                    isPossible = True
                    shop_num = item[0]
                    shop_items.remove(item)
                else:
                    isPossible = False
                    break
            if(not isPossible):
                break
            print('ambiguos')
    print('unique')

def listgame():
    x = int(input())
    factor = 2
    k = 0
    while(factor*factor <= x):
        if(x % factor == 0):
            x /= factor
            k += 1
        else:
            factor += 1
    print(k+1)


def mia():
    games = []
    while(True):
        game = str(input()).split()
        if(all (g != '0' for g in game)):
            games.append(game)
        else:
            break
    
    for game in games:
        player1 = max(int(game[0]),int(game[1]))*10 + min(int(game[0]),int(game[1]))
        player2 = max(int(game[2]),int(game[3]))*10 + min(int(game[2]),int(game[3]))
        if(player1 == 21 and player2 == 21):
            print('Tie.')
            continue
        elif(player1 == 21):
            print('Player 1 wins.')
            continue
        elif(player2 == 21):
            print('Player 2 wins.')
            continue
        
        if(player1 % 11 == 0 and player2 % 11 != 0):
            print('Player 1 wins.')
            continue
        elif(player2 % 11 == 0 and player1 % 11 != 0):
            print('Player 2 wins.')
            continue
        
        if(player1 == player2):
            print('Tie.')
            continue
        elif(player1 > player2):
            print('Player 1 wins.')
            continue
        else:
            print('Player 2 wins.')
            continue

def slatkisi():
    info = str(input()).split()
    price = int(info[0])
    
    expoent = int(info[1])
    money = 10**expoent
    
    rel_num = price % money
    
    if(rel_num >= money/2):
        print(price + abs(rel_num - money))
    else:
        print(price - rel_num)

def palindromesubstring():
    while(True):
        try:
            d = input()
        except EOFError:
            break
        palin_list = []

        for slice_size in range(2,len(d)):
            for i in range(len(d)-1):
                slic = d[i:i + slice_size]
                if(slic == slic[::-1]):
                    if(slic not in palin_list):
                        palin_list.append(slic)
        
        for s in sorted(palin_list):
            print(s)
        palin_list.clear()

def cranes():
    n = int(input())

    for nn in range(n):
        c = int(input())
        xyr = []
        area = 0
        for cc in range(c):
            _xyr = tuple(map(int, input().split()))
            if len(xyr) == 0:
                xyr.append(_xyr)
                continue
            for crane in xyr:
                d = [crane[i]-_xyr[i] for i in range(len(_xyr)-1)]
                print(d)
                distance = (d[0]**2 + d[1]**2)**(1/2)
                if(distance - crane[2]/2.0 - _xyr[2]/2.0 > 0):
                    xyr.append(_xyr)
                    area += _xyr[2]**2
        print(area)
cranes()
input()