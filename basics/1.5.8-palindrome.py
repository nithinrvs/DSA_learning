'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
'''
import re
class Solution(object):
    def isPalindrome(self, s):
        cleaned_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    
        # Use two pointers to check if the string is a palindrome
        left, right = 0, len(cleaned_s) - 1
        
        while left < right:
            if cleaned_s[left] != cleaned_s[right]:
                return False
            left += 1
            right -= 1
        
        return True

        
ob = Solution()
print(ob.isPalindrome("A man, a plan, a canal: Panama"))