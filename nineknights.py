def check(board):
    for knight in board:
        x, y = knight[0], knight[1]
        possible_moves = []
        possible_moves.append([x+1,y+2])
        possible_moves.append([x+2,y+1])
        
        possible_moves.append([x+1,y-2])
        possible_moves.append([x+2,y-1])
        
        possible_moves.append([x-1,y+2])
        possible_moves.append([x-2,y+1])

        possible_moves.append([x-1,y-2])
        possible_moves.append([x-2,y-1])

        num_moves = len(possible_moves)
        for possible_move in possible_moves:
            if(possible_move == knight):
                continue

            if(possible_move[0] < 0 or possible_move[0] > 4 or possible_move[1] < 0 or possible_move[1] > 4):
                continue
            if(possible_move in board):
                return 'invalid in board '
    return 'valid ' + str(num_moves)

if(__name__ == "__main__"):
    board = []
    for i in range(5):
        line = input()
        for j, s in enumerate(line):
            if s == 'k':
                board.append([i,j])
    print(check(board))
