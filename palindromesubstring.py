def _stdin():
    from sys import stdin
    for line in stdin:
        yield line


def rec(A):
    mem = set()
    a = len(A)

    for idx, char in enumerate(A):
        # odd
        start, end = idx - 1, idx + 1
        while start >= 0 and end < a and A[start] == A[end]:  # O(n)
            mem.update({A[start:end+1]})
            start -= 1
            end += 1
        # even
        start, end = idx, idx + 1
        while start >= 0 and end < a and A[start] == A[end]:  # O(n)
            mem.update({A[start:end+1]})
            start -= 1
            end += 1
    return sorted(mem)


def palindromesubstring():
    from sys import stdout
    line = _stdin()
    # Initial commentary
    try:
        while True:
            s = next(line).strip('\n')
            for _ in rec(s):
                stdout.write(_ + '\n')
            stdout.write('\n')
    except StopIteration:
        return
        pass


if __name__ == '__main__':
    palindromesubstring()
