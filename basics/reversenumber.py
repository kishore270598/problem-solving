class Solution:
    def isPalindrome(self, x: int):
        rev =x
        sum = 0
        if x < 0:
            return False
        while rev > 0:
            r = rev % 10
            sum = sum * 10 + r
            rev = rev // 10
        if sum == x:
            return True
