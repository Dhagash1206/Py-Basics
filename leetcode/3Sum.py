class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        n = len(nums)

        ans = []

        # Fix one number and use two pointers for the remaining two
        for i in range(n - 2):
            # Since the array is sorted, no later triplet can sum to 0
            if nums[i] > 0:
                break

            # Skip duplicate values for the first number
            if i and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, n - 1

            while j < k:

                x = nums[i] + nums[j] + nums[k]

                if x < 0:
                    j += 1

                elif x > 0:
                    k -= 1

                else:
                    ans.append([nums[i], nums[j], nums[k]])

                    j, k = j + 1, k - 1

                    # Skip duplicate values after finding a valid triplet
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return ans