from typing import List

"""
https://leetcode.com/problems/two-sum/
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):

            for j in range(i + 1, len(nums)):

                sum_value = nums[i] + nums[j]

                if sum_value == target:
                    return [i, j]

