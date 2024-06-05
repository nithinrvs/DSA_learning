'''
Given an integer n, calculate the sum of series 13 + 23 + 33 + 43 + … till n-th term.

Example 1:

Input:
n=5
Output:
225
Explanation:
1^3+2^3+3^3+4^3+5^3=225
'''

'''
class Solution:
    def sumOfSeries(self,n):
        if(n == 1):
            return 1    
        else:
            return n**3 + self.sumOfSeries(n-1)
'''

class Solution:
    def sumOfSeries(self,n):
        return (n * (n + 1) // 2) ** 2

ob = Solution()
print(ob.sumOfSeries(18468))