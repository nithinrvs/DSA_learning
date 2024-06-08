class Solution:
    def insert(self, alist, index, n):
        for j in range(0,index+1):
            if alist[j] > alist[index]:
                alist[j], alist[index] = alist[index], alist[j]
        
    #Function to sort the list using insertion sort algorithm.    
    def insertionSort(self, alist, n):
        for i in range(1,n):
            self.insert(alist,i,n)


n = 5
arr = [4, 1, 3, 9, 7]
Solution().insertionSort(arr, n)
for i in range(n):
    print(arr[i],end=" ")
print()