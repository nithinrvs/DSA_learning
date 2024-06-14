'''
Given a binary array nums, return the maximum number of consecutive 1's in the array.
Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
'''

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        maxiWindow = 0
        counter = 0
        for i in range(0,len(nums)):
            if nums[i] == 1:
                counter += 1
            else:
                if maxiWindow < counter:
                    maxiWindow = counter
                counter = 0
        if maxiWindow < counter:
            maxiWindow = counter
            
        return maxiWindow

solution = Solution()
nums = [1, 1, 0, 1, 1, 1]
print(solution.findMaxConsecutiveOnes(nums))  