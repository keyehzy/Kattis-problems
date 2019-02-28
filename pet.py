def pet():
    contestants = [1, 2, 3, 4, 5]
    grades = []
    for _ in range(5):
        grade = sum(map(int, input().split()))
        grades.append(grade)
    grades, contestants = zip(*sorted(zip(grades, contestants), reverse=True))
    print(str(contestants[0]) + ' ' + str(grades[0]))
    return


if __name__ == '__main__':
    pet()
