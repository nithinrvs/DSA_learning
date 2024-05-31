'''
Given a number N. Count the number of digits in N which evenly divide N.

Note :- Evenly divides means whether N is divisible by a digit i.e. leaves a remainder 0 when divided.
 

Example 1:

Input:
N = 12
Output:
2
Explanation:
1, 2 both divide 12 evenly
'''

class Solution:
    def evenlyDivides (self, N):
        count = 0
        number = N
        while N>0:
            i = N % 10
            N = N // 10
            if number % i == 0:
                count += 1
        return count
       

ob = Solution()
print(ob.evenlyDivides(12))