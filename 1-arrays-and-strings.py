from typing import Sequence

from collections import defaultdict


def is_unique(s: str) -> bool:
    s = sorted(s)
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return False

    return True


def check_perm(s1: str, s2: str) -> bool:
    table = set(s1)

    for c in s2:
        if c not in table:
            return False

    return True


def urlify(s: str) -> str:
    s = list(s)
    queue = []
    for i, c in enumerate(s):
        if c == " ":
            queue.append('%')
            queue.append('2')
            queue.append('0')
        else:
            queue.append(c)
        
        s[i] = queue.pop(0)

    while len(queue) > 0:
        s.append(queue.pop(0))

    return "".join(s)


def palindrome_perm(s: str) -> bool:
    table = defaultdict(int)
    for c in s.lower():
        table[c] += 1

    odds = 0
    for c, freq in table.items():
        if freq % 2 == 1:
            odds += 1

    return odds <= 2


def one_away(s1: str, s2: str) -> bool:
    if s1 == s2:
        return True

    if abs(len(s1) - len(s2)) >= 2:
        return False

    if len(s1) > len(s2):
        temp = s1
        s1 = s2
        s2 = temp

    for i in range(len(s1) + 1):
        rem1 = (s1[:i] + s1[i+1:])
        rem2 = (s2[:i] + s2[i+1:])
        if s1 == rem2 or rem1 == rem2:
            return True
    
    return False


def string_compression(s: str) -> str:
    if len(s) == 0:
        return s

    count = 0
    curr = s[0]
    rle = []
    for i in range(len(s)):
        if s[i] == curr:
            count += 1
        else:
            rle.append((curr, count))
            count = 1
            curr = s[i]
    
    rle.append((curr, count))
    
    cmp = "".join([str(c) + str(cnt) for c, cnt in rle])

    if len(cmp) < len(s):
        return cmp
    
    return s


def rotate_matrix(m: Sequence[Sequence[int]]) -> Sequence[Sequence[int]]:
    l = len(m)
    for y in range(l):
        for x in range(l):
            m[x][l - 1 - y] = m[y][x]
    
    return m


def zero_matrix(m: Sequence[Sequence[int]]) -> Sequence[Sequence[int]]:
    i_flags = [False] * len(m)
    j_flags = [False] * len(m[0])

    for i in range(len(m)):
        for j in range(len(m[0])):
            i_flags[i] |= int(m[i][j] == 0)
            j_flags[j] |= int(m[i][j] == 0)
        
    for i, f in enumerate(i_flags):
        if f:
            for j in range(len(m[0])):
                m[i][j] = 0

    for j, f in enumerate(j_flags):
        if f:
            for i in range(len(m)):
                m[i][j] = 0

    return m


def is_rotation(s: str) -> bool:
    pass


print(zero_matrix([[1, 2, 3], [0, 5, 6], [7, 0, 9]]))

