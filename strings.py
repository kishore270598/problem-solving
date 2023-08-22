import time
import math
class Strings_problems:
    def removeOuterParentheses(self, s):
        left=0
        right=0
        start=0
        end=0
        new_string=""
        for i in range(0,len(s),1):
            if(s[i]=='('):
                left+=1
            else:
                right+=1
            if(left==right):
                new_string+=self.removeouttermost(s,start,i)
                start=i+1
        return new_string
    
    def removeouttermost(self,s,start,end):
        new_string=""
        for i in range(start+1,end,1):
            new_string+=s[i]
        return new_string
    
    def maxDepth(self,s):
        stack=[]
        max_=0
        for i in range(0,len(s),1):
            if(s[i]=='('):
                stack.append(s[i])
                if(len(stack)>max_):
                    max_=len(stack)
            elif(s[i]==')'):
                if(len(stack)>0):
                    stack.pop()
        return max_
    
    def reverseWords(self, s: str) -> str:
        new_string=""
        end=len(s)
        for i in range(len(s)-1,-1,-1):
            word=""
            if(i==0 and s[i]!=' '):
                word=self.addinnerwords(s,i,end)
            if(s[i]==' '):
                word=self.addinnerwords(s,i+1,end)
                end=i
            if(len(word)>0):
                if(len(new_string)>0):
                    new_string+=' '
                new_string+=word
        return new_string

    def addinnerwords(self,s,start,end):
        new_string=""
        for i in range(start,end,1):
            new_string+=s[i]
        return new_string
    
    def largestOddNumber(self, num: str) -> str:
        max_odd=""
        flg=0
        if(num==""):
            return num
        for i in range(len(num)-1,-1,-1):
            if(int(num[i])%2==1):
                flg=1
                break
        if(flg==1):
            max_odd+=num[0:i+1]
        return max_odd
    def longestCommonPrefix(self, strs):
        min_len=len(strs[0])
        common_string=""
        for k in range(0,len(strs),1):
            if(len(strs[k])<min_len):
                min_len=len(strs[k])
        for i in range(0,min_len,1):
            common=strs[0][i]
            for j in range(1,len(strs),1):
                if(strs[j][i]!=common):
                    return common_string
            common_string+=common
        return common_string

     
     


a=Strings_problems()
s =["cir","car","ca"]
ans=a.longestCommonPrefix(s)
print(ans)