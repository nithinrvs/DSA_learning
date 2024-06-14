'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
'''

class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        sum_of_n = (n*(n+1))/2
        sum_of_arr = sum(nums)
        
        return sum_of_n - sum_of_arr
        
print(Solution().missingNumber([3,0,1]))