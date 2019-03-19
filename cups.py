from sys import stdin, stdout

input = iter(stdin.read().splitlines()).__next__


def write(x):
    return stdout.write(x)


def cups():
    # Initial commentary

    n = int(input())
    cols = []
    nums = []
    for i in range(n):
        col, num = input().split()
        if col.isdigit():
            temp = col
            col = num
            num = float(temp) / 2.
        cols.append(col)
        nums.append(nums)
    [print(x) for y, x in sorted(zip(nums, cols))]
    return

if __name__ == '__main__':
    cups()