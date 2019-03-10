def _stdin():
    from sys import stdin
    for line in stdin:
        yield line

def battlesimulation():
    from sys import stdout
    line = _stdin()
    # Initial commentary

    move = next(line).strip('\n')

    c_move = {'R': 'S', 'B': 'K', 'L': 'H'}
    combo = {'RBL', 'BLR', 'LRB', 'BRL', 'LBR', 'RLB'}
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
    stdout.write(''.join(result))
    return


if __name__ == '__main__':
    battlesimulation()
