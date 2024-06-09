class Solution:
    def print2largest(self,arr, n):
        max = self.findMax(arr,n)
        arr[max] = -1
        self.printarr(arr,n)
        
        return self.findMax(arr,n)

    def findMax(self,arr,n):
        max = 0
        for i in range(0,n):
            if arr[i] > arr[max]:
                max = i
        return max


n = 5
arr = [4, 1, 3, 9, 7]
ans = Solution().print2largest(arr, n)

print(ans)

    