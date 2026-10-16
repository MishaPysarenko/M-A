
def sortedSquares(nums):
    result = []

    for num in nums:
        result.append(num ** 2)

    result.sort()
    return result


print(sortedSquares([-4, -1, 0, 3, 10]))
# [0, 1, 9, 16, 100]

print(sortedSquares([-7, -3, 2, 3, 11]))
# [4, 9, 9, 49, 121]
