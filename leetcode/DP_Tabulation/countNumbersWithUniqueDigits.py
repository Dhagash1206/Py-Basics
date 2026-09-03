class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1

        def count(length, used):
            # Current number itself is valid
            total = 1

            if length == n:
                return total

            for digit in range(10):
                if digit not in used:
                    used.add(digit)

                    total += count(length + 1, used)

                    used.remove(digit)

            return total

        
        ans = 1

        # First digit cannot be 0
        for first in range(1, 10):
            used = {first}
            ans += count(1, used)

        return ans