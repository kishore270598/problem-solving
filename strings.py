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
    
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict_map={}
        if (len(s)!=len(t)):
            return False
        for index in range(0,len(s),1):
            char1=s[index]
            char2=t[index]
            if(char1 not in dict_map):
                if(char2 in dict_map.values()):
                    return False
                dict_map[char1]=char2
            elif(dict_map[char1]!=char2):
                return False
        return True
    
    def rotateString(self, s: str, goal: str) -> bool:
        final_ans=s+s
        if(goal in final_ans):
            return True
        else:
            return False
        
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        s_=sorted(s)
        t_=sorted(t)
        for i in range(0,len(s),1):
            if(s_[i]!=t_[i]):
                return False
        return True
    
    def frequencySort(self, s: str) -> str:
        dict_map={}
        max_=0
        ans=""
        freq=[]
        for i in range(0,len(s),1):
            if s[i] not in dict_map:
                dict_map[s[i]]=1
            else:
                dict_map[s[i]]+=1
        for key in dict_map:
            freq.append(dict_map[key])
        freq.sort(reverse=True)
        for i in range(0,len(freq),1):
            ans+=self.printthechar(freq[i],dict_map)
        print(ans)
    def printthechar(self,val,dict_map):
        for key in dict_map:
            if(dict_map[key]==val):
                dict_map[key]=0
                return val*key
            
a=Strings_problems()
s ="tree"
b="nagaram"
ans=a.frequencySort(s)
print(ans)