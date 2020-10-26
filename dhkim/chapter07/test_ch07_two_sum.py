from unittest import TestCase
from .ch07_two_sum import Solution




class TestSolution(TestCase):
    def test_two_sum(self):
        sol = Solution()
        res = sol.twoSum([2,7,11,15], 9)

        self.assertEqual(res, [0, 1])
