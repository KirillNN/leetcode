from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        my_set = set(nums)
        my_dict = {x: nums.count(x) for x in my_set}
        max_key = max(my_dict, key=my_dict.get)
        return max_key


solution = Solution()
print(solution.majorityElement([3, 2, 3]))
print(solution.majorityElement([2, 2, 1, 1, 1, 2, 2]))
