from typing import Sequence

from collections import defaultdict


def is_unique(s: str) -> bool:
    s = sorted(s)
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return False

    return True


def is_unique_bit(s: str) -> bool:
    if len(s) > 128:
        return False

    bitmap = 0
    for c in s:
        if (bitmap >> int(c)) & 1 == 1:
            return False
        bitmap |= 1 << int(c)

    return True


def check_perm(s1: str, s2: str) -> bool:
    table = defaultdict(int)

    for c in s1:
        table[c] += 1

    for c in s2:
        table[c] -= 1
        if table[c] < 0:
            return False

    return True


def check_perm_sorted(s1: str, s2: str) -> bool:
    if len(s1) != s2:
        return False

    return sorted(s1) == sorted(s2)


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

    return odds <= 1


def palindrome_perm_bit(s: str) -> bool:
    bitmap = 0
    for c in s.lower():
        bitmap ^= 1 << int(c)

    return bitmap == 0 or (bitmap - 1) & bitmap == 0


def one_away(s1: str, s2: str) -> bool:
    if s1 == s2:
        return True

    if abs(len(s1) - len(s2)) >= 2:
        return False

    if len(s1) > len(s2):
        s1, s2 = s2, s1

    found_diff = False
    i = j = 0
    
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if found_diff:
                return False
            found_diff = True

            if len(s1) == len(s2):
                j += 1
        else:
            j += 1

        i += 1

    return True


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
    # top -> 0 0,1,2 -> y, x
    # left -> 2,1,0 0 -> -x, y
    # bottom -> 2 2,1,0 -> -y, -x
    # right -> 0,1,2 2 -> x, -y

    l = len(m)
    for y in range(l):
        for x in range(y, l - y - 1):
            print((y, x), (l - x - 1, y), (l - y - 1, l - x - 1), (x, l - y - 1))
            temp = m[y][x]
            m[y][x] = m[l - x - 1][y]
            m[l - x - 1][y] = m[l - y - 1][l - x - 1]
            m[l - y - 1][l - x - 1] = m[x][l - y - 1]
            m[x][l - y - 1] = temp

    return m


def zero_matrix(m: Sequence[Sequence[int]]) -> Sequence[Sequence[int]]:
    i_flags = [False] * len(m)
    j_flags = [False] * len(m[0])

    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 0:
                i_flags[i] = True
                j_flags[j] = True
        
    for i, f in enumerate(i_flags):
        if f:
            for j in range(len(m[0])):
                m[i][j] = 0

    for j, f in enumerate(j_flags):
        if f:
            for i in range(len(m)):
                m[i][j] = 0

    return m


def is_rotation(s1: str, s2: str) -> bool:
    return s2 in (s1 + s1)


print(rotate_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

