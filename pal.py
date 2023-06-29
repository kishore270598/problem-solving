class Solution:
    def isPalindrome(self, S):
        lens=len(S)
        start=0
        end=len(S)-1
        flag=0
        while (start<=end):
            if(S[start]==S[end]):
                flag=1
            else:
                return 0
            start+=1
            end-=1
        if(flag==1):
            return 1
	   
s=Solution()
k='A man'
z=len(k)
print(z)
print(s.isPalindrome(k))