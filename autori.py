import re


def autori():
    regex = re.compile('[^A-Z]')
    return regex.sub('', input())


if __name__ == '__main__':
    print(autori())
