class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        pair_sums = {}

        for v1 in nums1:
            for v2 in nums2:
                curr = v1 + v2

                if curr in pair_sums:
                    pair_sums[curr] += 1
                else:
                    pair_sums[curr] = 1

        count = 0

        for v3 in nums3:
            for v4 in nums4:
                req = -(v3 + v4)

                if req in pair_sums:
                    count += pair_sums[req]

        return count