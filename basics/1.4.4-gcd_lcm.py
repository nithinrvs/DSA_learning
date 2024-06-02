'''
Given two numbers A and B. The task is to find out their LCM and GCD.

Example 1:

Input:
A = 5 , B = 10
Output:
10 5
Explanation:
LCM of 5 and 10 is 10, while their GCD is 5.
'''

class Solution:
    def lcmAndGcd(self, A , B):
        #Finding LCM
        gcd = self.findGCD(max(A,B),min(A,B))
        lcm = A * B // gcd

        return [lcm,int(gcd)]
    

    def findGCD(self,a,b):
        while b!=0:
            rem = a% b
            q = a / b
            a = b
            b = rem
        return a


ob = Solution()
ptr = ob.lcmAndGcd(5,10)
print(ptr[0],ptr[1])

