def modulo():
    nums = {}
    n = 10

    for _ in range(n):
        nums[int(input()) % 42] = ''

    print(len(nums))
    return

if __name__ == '__main__':
    modulo()

