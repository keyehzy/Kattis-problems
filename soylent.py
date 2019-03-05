import math
def soylent():
    n = int(input())

    for _ in range(n):
        i = float(input())

        print(math.ceil(i/400))
    return
    
if __name__ == '__main__':
    soylent()
