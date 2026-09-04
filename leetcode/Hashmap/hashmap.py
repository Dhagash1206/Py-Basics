from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        dict = {}

        for i in range(len(list1)):
            dict[list1[i]] = i

        ans = []
        min_sum = float('inf')

        for j in range(len(list2)):

            if list2[j] in dict:

                curr_sum = dict[list2[j]] + j

                if curr_sum < min_sum:

                    min_sum = curr_sum
                    ans = [list2[j]]

                elif curr_sum == min_sum:

                    ans.append(list2[j])

        return ans