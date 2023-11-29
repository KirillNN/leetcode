from typing import Any


class Solution:
    def hammingWeight(self, n: int) -> int:
        count_one = 0
        while n:
            if n % 2:
                count_one += 1
            n //= 2
        return count_one

    def hamming_weight(self, n: int) -> int:
        return bin(n)[2:].count('1')

    def hamming_weight1(self, n: int) -> int:
        return n.bit_count()


solution = Solution()
print(solution.hammingWeight(11))
print(solution.hamming_weight(11))
print(solution.hamming_weight1(11))
