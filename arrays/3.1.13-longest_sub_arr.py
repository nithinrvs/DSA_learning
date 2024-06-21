'''
Given an array containing N integers and an integer K., Your task is to find the length of the longest Sub-Array with the sum of the elements equal to the given value K.

Example 1:
 

Input :
A[] = {10, 5, 2, 7, 1, 9}
K = 15
Output : 4
Explanation:
The sub-array is {5, 2, 7, 1}.
'''

class Solution:
    def lenOfLongSubarr(self, arr, n, k):
        sum_index_map = {}
        
        max_length = 0
        current_sum = 0

        for i in range(n):
            current_sum += arr[i]

            if current_sum == k:
                max_length = i + 1

            if (current_sum - k) in sum_index_map:
                max_length = max(max_length, i - sum_index_map[current_sum - k])

            if current_sum not in sum_index_map:
                sum_index_map[current_sum] = i

        return max_length

solution = Solution()
arr = [-13, 0, 6, 15, 16, 2, 15, -12, 17, -16, 0, -3, 19, -3, 2, -9, -6]
n = len(arr)
k = 15
print(solution.lenOfLongSubarr(arr, n, k))