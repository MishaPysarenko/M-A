
def firstUniqChar(s):
    count = {}

    for char in s:
        count[char] = count.get(char, 0) + 1

    for i in range(len(s)):
        if count[s[i]] == 1:
            return i

    return -1


print(firstUniqChar("leopard"))      # 0
print(firstUniqChar("loveleopard"))  # 2
print(firstUniqChar("aabb"))         # -1
