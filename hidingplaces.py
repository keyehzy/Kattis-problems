from sys import stdin, stdout

input = iter(stdin.read().splitlines()).__next__


def write(x):
    return stdout.write(x)

def man(u, v):
    return abs(u[0]-v[0]) + abs(u[1]-v[1])

def AdjList(u):
    # u is a tuple
    adj = []
    moves = [
        (u[0] + 1, u[1] + 2),
        (u[0] + 2, u[1] + 1),
        (u[0] - 1, u[1] - 2),
        (u[0] - 2, u[1] - 1),
        (u[0] + 1, u[1] - 2),
        (u[0] + 2, u[1] - 1),
        (u[0] - 1, u[1] + 2),
        (u[0] - 2, u[1] + 1)
    ]
    for move in moves:
        if move[0] >= 1 and move[1] >= 1 and move[0] <= 8 and move[1] <= 8:
            adj.append(move)
    return adj

def hidingplaces():

    # Initial commentary
    INF = 1 << 20
    piece = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5,
             'f': 6, 'g': 7, 'h': 8}
    s = input()
    s = tuple([int(s[0]), int(s[1])])
    
    d = [[INF for x in range(1, 10)] for y in range(1, 10)]

    d[s[0]][s[1]] = 0
    q = [s]

    while q:
        u = q.pop()
        for adj in AdjList(u):
            v = adj
            if d[v[0]][v[1]] == INF:
                d[v[0]][v[1]] = d[u[0]][u[1]] + 1
                q.append(v)
                print(v, d[v[0]][v[1]])
    return

if __name__ == '__main__':
    hidingplaces()