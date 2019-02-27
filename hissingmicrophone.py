import re

def hissingmicrophone():

    start = input()

    regex = re.compile('[s]{2}')
    hiss = re.search(regex, start)

    return 'hiss' if hiss else 'no hiss'


if __name__ == '__main__':
    print(hissingmicrophone())
