class Solution: 
    def select(self, arr, i):
        min_idx = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        return min_idx
    
    def selectionSort(self, arr,n):
        for i in range(n):
            min_index = self.select(arr,i)
            if min_index!=i:
                arr[min_index], arr[i] = arr[i], arr[min_index]

n = 5
arr = [4, 1, 3, 9, 7]
Solution().selectionSort(arr, n)
for i in range(n):
    print(arr[i],end=" ")
print()