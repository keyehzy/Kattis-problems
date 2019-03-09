def eligibility():
    n = int(input())
    for _ in range(n):
        name, second, born, c = map(str, input().split())
        second = second.split(r'/')
        born = born.split(r'/')

        if int(second[0]) > 2010:
            if int(born[0]) > 1991:
                print(name + ' eligible')
        elif int(c) > 41:
            print(name + ' ineligible')
        else:
            print(name + ' coach petitions')

    return


if __name__ == '__main__':
    eligibility()