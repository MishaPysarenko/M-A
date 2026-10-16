
def sortArrayByParity(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        if nums[left] % 2 == 0:
            left += 1
        elif nums[right] % 2 != 0:
            right -= 1
        else:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    return nums


print(sortArrayByParity([3, 1, 2, 4]))
# [4, 2, 1, 3]

print(sortArrayByParity([0]))
# [0]
