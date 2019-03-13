def _stdin():
    from sys import stdin
    for line in stdin:
        yield line


def abc():
    from sys import stdout
    line = _stdin()
    # Initial commentary

    nums = list(sorted(map(int, next(line).split())))
    order = list(next(line).strip('\n'))

    abc = {"A": nums[0], "B": nums[1], "C": nums[2]}

    stdout.write(' '.join([str(abc[x]) for x in order])+'\n')

    return


if __name__ == '__main__':
    abc()