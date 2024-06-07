class Solution:
    def bubbleSort(self,arr, n):
        for i in range(n):
            for j in range(n):
                if arr[i] < arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
            print("\nstep: "+str(i))
            self.print_arr(arr)

    def print_arr(self,arr):
        for i in range(len(arr)):
            print(arr[i], end=" ")
        

n = 5
arr = [4, 1, 3, 9, 7]
Solution().bubbleSort(arr, n)
