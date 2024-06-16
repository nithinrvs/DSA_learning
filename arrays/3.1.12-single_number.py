'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4
'''

class Solution(object):
    def singleNumber(self, nums):
        val = 0
        for num in nums:
            val ^= num
        return val

arr = [4, 1, 2, 1, 2]
ans = Solution().singleNumber(arr)
print("The single element is:", ans)