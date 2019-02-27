import re

def apaxiaaans():

    string = input()
    search = string
    count = {}
    for s in string:
        if count.get(s):
            count[s] += 1
        else:
            count[s] = 1

    for key in count:
        if count[key] > 1:
            regex = re.compile('([' + key + ']{2,})')
            search = regex.sub(key, search)
    print(search)
    return


if __name__ == '__main__':
    apaxiaaans()
