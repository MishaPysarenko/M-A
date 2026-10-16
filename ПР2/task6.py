
def removeDuplicates(nums):
    k = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[k - 1]:
            nums[k] = nums[i]
            k += 1

    return k


nums = [1, 1, 2]
k = removeDuplicates(nums)
print(k, nums[:k])  # 2 [1, 2]

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k = removeDuplicates(nums)
print(k, nums[:k])  # 5 [0, 1, 2, 3, 4]
