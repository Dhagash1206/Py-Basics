class Solution:
    def sortedSquares(self, nums):
        n = len(nums)
        ans = [0] * n
        left, right = 0, n - 1

        for i in range(n - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                ans[i] = nums[left] ** 2
                left += 1
            else:
                ans[i] = nums[right] ** 2
                right -= 1

        return ans