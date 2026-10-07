class Solution:
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0

        minV, maxV = min(nums), max(nums)
        if minV == maxV:
            return 0

        bucket_size = max(1, (maxV - minV) // (len(nums) - 1))
        bucket_count = (maxV - minV) // bucket_size + 1

        buckets = [[float("inf"), float("-inf")] for _ in range(bucket_count)]

        for number in nums:
            index = (number - minV) // bucket_size
            buckets[index][0] = min(buckets[index][0], number)
            buckets[index][1] = max(buckets[index][1], number)

        maximum_gap = 0
        prev_min = minV

        for minB, maxB in buckets:
            if minB != float("inf"):
                maximum_gap = max(maximum_gap, minB - prev_min)
                prev_min = maxB

        return maximum_gap