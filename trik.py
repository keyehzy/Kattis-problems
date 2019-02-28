def trik():
    moves = {'A': [0, 1], 'B': [1, 2], 'C': [0, 2]}
    move_seq = input()
    init_pos = [1, 0, 0]
    for m in move_seq:
        temp = init_pos[moves[m][0]]
        init_pos[moves[m][0]] = init_pos[moves[m][1]]
        init_pos[moves[m][1]] = temp
    print(init_pos.index(1)+1)
    return


if __name__ == '__main__':
    trik()
