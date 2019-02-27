import math

def ladder():
    h, v = map(float, input().split())

    result = math.ceil(h / math.sin(math.radians(v)))
    print(int(result))
    return


if __name__ == '__main__':
    ladder()
