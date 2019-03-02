def icpcawards():
    n = int(input())

    unis = []
    teams = []
    for _ in range(n):
        u, t = map(str, input().split())
        if u in unis:
            if unis[unis.index(u)] < 1: 
                unis[unis.index(u)] += 1
                teams.append(t)
            else:
                continue
        else:
            unis.append(u)
            teams.append(t)
if __name__ == '__main__':
    icpcawards()

