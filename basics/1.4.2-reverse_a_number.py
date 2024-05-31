'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1
'''

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        neg_flag = 1
        if x<0:
            neg_flag = -1
            x = abs(x)

        result = 0
        while x > 0:
            i = x % 10
            x = x // 10
            result = result*10 + i

        result = neg_flag*result
        if result>2**31-1 or result<-2**31:
            return 0
        return result





        
        