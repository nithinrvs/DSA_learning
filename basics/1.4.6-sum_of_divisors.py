'''
Given a positive integer N., The task is to find the value of Σi from 1 to N F(i) where function F(i) for the number i is defined as the sum of all divisors of i.

Example 1:

Input:
N = 4
Output:
15
Explanation:
F(1) = 1
F(2) = 1 + 2 = 3
F(3) = 1 + 3 = 4
F(4) = 1 + 2 + 4 = 7
ans = F(1) + F(2) + F(3) + F(4)
    = 1 + 3 + 4 + 7
    = 15
'''

class Solution:
    def sumOfDivisors(self, N):
        sum = 0
        for i in range(1, N+1):
            sum += i * (N // i)
        return sum
    	

ob = Solution()
print(ob.sumOfDivisors(4))