'''
Given an array A[] of size n. The task is to find the largest element in it.
 
Example 1:

Input:
n = 5
A[] = {1, 8, 7, 56, 90}
Output:
90
Explanation:
The largest element of given array is 90.
'''

def largest( arr, n):
    max = arr[0]
    for i in range(0,n):
        if arr[i] > max:
            max = arr[i]
    
    return max


n = 5
arr = [4, 1, 3, 9, 7]
max= largest(arr, n)
print(max)