class Solution:
    def merge(self, arr, l, m, r):
        left = arr[l:m+1]
        right = arr[m+1:r+1]
        
        i = 0
        j = 0
        k = l
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    def mergeSort(self, arr, l, r):
        if l < r:
            m = l + (r - l) // 2
            
            self.mergeSort(arr, l, m)
            self.mergeSort(arr, m + 1, r)
            
            self.merge(arr, l, m, r)


n = 5
arr = [4, 1, 3, 9, 7]
Solution().mergeSort(arr,0, n-1)
for i in range(n):
    print(arr[i],end=" ")