class Solution:
    def isPalindrome(self, S):
        z=""
        for i in range (0,len(S),1):
            if(S[i].isalpha()==True):
                z+=S[i]
        lens=len(z)
        start=0
        end=len(z)-1
        flag=0
        print(z)
        while (start<=end):
            if(z[start]==z[end]):
                flag=1
            else:
                return 0
            start+=1
            end-=1
        if(flag==1):
            return 1
	   
s=Solution()
k='A man, a plan, a canal: Panama'
k=k.lower()
print(k)
print(s.isPalindrome(k))


#string iterate
#character check is valid 
#check palain
