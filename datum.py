def datum():
    weekdays = {4: 'Monday', 5: 'Tuesday', 6: 'Wednesday', 0: 'Thursday', 1: 'Friday', 2: 'Saturday', 3: 'Sunday'}

    monthdays = {0: 31, 1: 28, 2: 31, 3: 30, 4: 31, 5: 30, 6: 31, 7: 31, 8: 30, 9: 31, 10: 30, 11: 31}

    d, m = map(int, input().split())

    days = 0
    for i in range(m-1):
        days += monthdays[i]
    days += d

    print(weekdays[(days-1) % 7])
    return


if __name__ == '__main__':
    datum()
