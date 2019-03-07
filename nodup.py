def nodup():
    s1 = input().split()
    print('yes' if len(s1) == len(set(s1)) else 'no')
    return


if __name__ == '__main__':
    nodup()

