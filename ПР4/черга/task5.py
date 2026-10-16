
def movesToStamp(stamp, target):
    target = list(target)
    m = len(stamp)
    n = len(target)
    result = []
    changed = True

    while changed:
        changed = False

        for i in range(n - m + 1):
            can_stamp = True
            has_letters = False

            for j in range(m):
                if target[i + j] == '?':
                    continue

                if target[i + j] != stamp[j]:
                    can_stamp = False
                    break

                has_letters = True

            if can_stamp and has_letters:
                for j in range(m):
                    target[i + j] = '?'

                result.append(i)
                changed = True

                if len(result) > 10 * n:
                    return []

    if all(char == '?' for char in target):
        return result[::-1]

    return []


# Приклад 1
print(movesToStamp("abc", "ababc"))
# [0, 2]

# Приклад 2
print(movesToStamp("abca", "aabcaca"))
# [3, 0, 1]
