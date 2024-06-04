'''
Print numbers from 1 to N without the help of loops.

Example 1:

Input:
N = 10
Output: 1 2 3 4 5 6 7 8 9 10
'''

class Solution:    
    def printNos(self,N):
        if N <= 0:
            return
        self.printNos(N-1)
        print(N, end=" ")

ob = Solution()
print(ob.printNos(4))