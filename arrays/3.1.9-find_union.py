'''
Given two sorted arrays of size n and m respectively, find their union. The Union of two arrays can be defined as the common and distinct elements in the two arrays. Return the elements in sorted order.

Example 1:

Input: 
n = 5, arr1[] = {1, 2, 3, 4, 5}  
m = 5, arr2 [] = {1, 2, 3, 6, 7}
Output: 
1 2 3 4 5 6 7
Explanation: 
Distinct elements including both the arrays are: 1 2 3 4 5 6 7.
'''

class Solution:
    
    def findUnion(self,arr1,arr2,n,m):
 
        return sorted(list(set(arr1+arr2)))

arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 3, 6, 7]
print(Solution().findUnion(arr1,arr2,5,5))