class Solution:
    def largestDivisibleSubset(self, nums):
        nums.sort()
        n = len(nums)

        dp = [1] * n
        previous = [-1] * n

        largest_size = 1
        largest_index = 0

        for index in range(n):
            for previous_index in range(index):
                if nums[index] % nums[previous_index] == 0:
                    if dp[previous_index] + 1 > dp[index]:
                        dp[index] = dp[previous_index] + 1
                        previous[index] = previous_index

            if dp[index] > largest_size:
                largest_size = dp[index]
                largest_index = index

        answer = []

        while largest_index != -1:
            answer.append(nums[largest_index])
            largest_index = previous[largest_index]

        return answer[::-1]