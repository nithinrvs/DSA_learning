'''
Print numbers from N to 1 (space separated) without the help of loops.

Example 1:

Input:
N = 10
Output: 10 9 8 7 6 5 4 3 2 1
'''

class Solution:
    def printNos(self, n):
        if(n != 1):
            print(n, end=" ")
            self.printNos(n-1)
        else:
            print(1, end= " ")
ob = Solution()
ob.printNos(10)