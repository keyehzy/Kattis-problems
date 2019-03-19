from sys import stdin, stdout

input = iter(stdin.read().splitlines()).__next__

def write(x):
    return stdout.write(x)

def battlesimulation():
    # Initial commentary

    move = input()

    c_move = {'B': 'K', 'L': 'H', 'R': 'S'}
    combo = {'BLR', 'BRL', 'LBR', 'LRB', 'RBL', 'RLB'}
    i = 0
    a = len(move)
    result = ''
    while i < a:
        if a - i >= 3:
            if move[i:i+3] in combo:
                result += 'C'
                i += 3
            else:
                result += c_move[move[i]]
                i += 1
        else:
            result += c_move[move[i]]
            i += 1
    write('%s\n' % result)
    return


if __name__ == '__main__':
    battlesimulation()
