
def duplicateZeros(arr):
    i = 0

    while i < len(arr):
        if arr[i] == 0:
            arr.insert(i, 0)
            arr.pop()
            i += 1
        i += 1

    return arr


print(duplicateZeros([1, 0, 2, 3, 0, 4, 5, 0]))
# [1, 0, 0, 2, 3, 0, 0, 4]

print(duplicateZeros([1, 2, 3]))
# [1, 2, 3]
