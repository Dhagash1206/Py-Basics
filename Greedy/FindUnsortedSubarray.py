class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left = n
        right = -1
        minimum = float('inf')
        maximum = float('-inf')

        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                left = min(left, i)
                right = i + 1

        if right == -1:
            return 0

        for i in range(left, right + 1):
            minimum = min(minimum, nums[i])
            maximum = max(maximum, nums[i])

        while left > 0 and nums[left - 1] > minimum:
            left -= 1

        while right < n - 1 and nums[right + 1] < maximum:
            right += 1

        return right - left + 1