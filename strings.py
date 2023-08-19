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

a=Strings_problems()
s ="he, llo ,world"
ans=a.reverseWords(s)
print(ans)