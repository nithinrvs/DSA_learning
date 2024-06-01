class Solution(object):
    def isPalindrome(self, x):
        original = x
        if x >= 0:
            result = 0
            while x > 0:
                i = x % 10
                x = x // 10
                result = result*10 + i
            if original == result:
                return True
        else:
            return False