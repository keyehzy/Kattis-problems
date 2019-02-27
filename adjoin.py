def adjoin():
    n_comp, n_cable = map(int, input().split())
    
    tree_comp = [ [] for _ in range(n_comp)]
    for ll in range(n_cable):
        x, y = map(int, input().split)
        tree_comp[x].append([y])
    tree_comp.sort(key = len, reverse = True)
    print(tree_comp)

if(__name__ == '__main__'):
    adjoin()
    input()
