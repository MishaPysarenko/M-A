
from collections import deque


def constrainedSubsetSum(nums, k):
    q = deque()
    dp = [0] * len(nums)
    max_sum = nums[0]

    for i in range(len(nums)):
        while q and q[0] < i - k:
            q.popleft()

        dp[i] = nums[i]

        if q:
            dp[i] += max(0, dp[q[0]])

        max_sum = max(max_sum, dp[i])

        while q and dp[q[-1]] <= dp[i]:
            q.pop()

        q.append(i)

    return max_sum


# Приклад 1
print(constrainedSubsetSum([10, 2, -10, 5, 20], 2))
# 37

# Приклад 2
print(constrainedSubsetSum([-1, -2, -3], 1))
# -1

# Приклад 3
print(constrainedSubsetSum([10, -2, -10, -5, 20], 2))
# 23
