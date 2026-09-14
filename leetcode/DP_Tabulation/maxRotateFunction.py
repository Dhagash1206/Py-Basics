class Solution:
    def maxRotateFunction(self, nums):
        n = len(nums)
        total = sum(nums)

        curr  = 0

        for index in range(n):
            curr  += index * nums[index]

        maxV = curr 

        for index in range(n - 1, 0, -1):
            curr  += total - n * nums[index]
            maxV = max(maxV, curr )

        return maxV