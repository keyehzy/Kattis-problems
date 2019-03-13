def _stdin():
    from sys import stdin
    for line in stdin:
        yield line

def check(x, m, k):
    return (x-m) % k == 0

def solve(n, m, k):  # do not know how this works
    dp = [0]*5      # 10 more than the highest
    i, j = 0, 0
    for i in range(n+1):  # going from 0 to n
        for j in range(i-1, 0, -1):  # going from [i-1] -> [i-1,i-2] -> [i-1, i-2, i-3] -> ... -> [i-1 ... 1]
            diff = i-j   # i-j > 0 = 1, 2, 3 for ex: i = 4
            if not check(diff, m, k):
                dp[i] += dp[j]
            print(dp)
        if not check(i, m, k):
            dp[i] += 1
        print(dp)
    return dp[n]

def compositions():
    from sys import stdout
    line = _stdin()
    # Initial commentary
#    n = int(next(line))
#    for _ in range(n):
#        idx, n, m, k = map(int, next(line).split())
    print(solve(4, 0, 3))
    return


if __name__ == '__main__':
    compositions()