'''
Given an integer N, return true it is an Armstrong number otherwise return false.

An Amrstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.

Examples
Example 1:
Input:N = 153
Output:True
Explanation: 13+53+33 = 1 + 125 + 27 = 153
Example 2:
Input:N = 371
Output: True
Explanation: 33+53+13 = 27 + 343 + 1 = 371
'''

class Solution:
    def checkArmstrong (self, N):
        actual = N
        length = len(str(N))
        result = 0
        while N>0:
            digit = N % 10
            N = N//10
            result += digit ** length
        return True if result == actual else False
       

ob = Solution()
print(ob.checkArmstrong(100))
