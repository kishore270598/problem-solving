class Solution:
    def isPalindrome(self, x: int):
        rev = n
        sum = 0
        if x < 0:
            return False
        while rev > 0:
            r = rev % 10
            sum = sum * 10 + r
            rev = rev // 10
        if sum == n:
            return True
