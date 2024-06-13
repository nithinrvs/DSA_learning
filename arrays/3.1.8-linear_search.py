'''
Given an array arr[] sorted in ascending order of size N and an integer K. Check if K is present in the array or not.

Example 1:

Input:
N = 5, K = 6
arr[] = {1,2,3,4,6}
Output: 1
Exlpanation: Since, 6 is present in 
the array at index 4 (0-based indexing),
output is 1.
'''

class Solution:
    def searchInSorted(self,arr, N, K):
        for i in range(0,N):
            if arr[i] == K:
                return 1
        return -1

arr = [1,2,3,4,6]

print(Solution().searchInSorted(arr,5,6))