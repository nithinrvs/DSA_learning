'''
Print GFG n times without the loop.

Example:

Input:
5
Output:
GFG GFG GFG GFG GFG
'''

class Solution:
    def printGfg(self, n):
        if n <= 0:
            return
        self.printGfg(n-1)
        print("GFG", end=" ")

ob = Solution()
ob.printGfg(100)