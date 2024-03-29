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

    def romanToInt(self, s):
        #Decalration of symbol and values
        val={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        sum_=0
        for i in range (len(s)):
            if(i!=len(s)-1):
                if(s[i]=='I' and ( s[i+1]=='V' or  s[i+1]=='X' )):
                   sum_+=-1*self.findthesum(s[i],val)
                elif(s[i]=='X' and ( s[i+1]=='L' or  s[i+1]=='C' )):
                    sum_+=-1*self.findthesum(s[i],val)
                elif(s[i]=='C' and ( s[i+1]=='D' or  s[i+1]=='M' )):    
                    sum_+=-1*self.findthesum(s[i],val)
                else:
                    sum_+=self.findthesum(s[i],val)
            else:
                    sum_+=self.findthesum(s[i],val)
        return sum_

    def findthesum(self,a,val):
        if(a in val):
            sum_=val[a]

        return sum_     

    def myAtoi(self, s: str) -> int:
        maxInt=2**31 - 1
        minInt=-2**31
        ans=0
        start=0
        sign=1
        str1=s.lstrip()
        if (len(str1)==0): 
          return ans
        if(str1[start]=="-"):
            sign=-1
            start+=1
        elif(str1[start]=="+"):
            sign=1
            start+=1
        for i in range(start, len(str1),1):
            char=str1[i]
            if not char.isdigit():
                break
            else:
                ans=(ans*10) + int(char)

        if ((ans * sign)>maxInt):
            return maxInt
        elif ((ans * sign)<=minInt):
            return minInt
        return ans*sign

    
    def countSubStrings(self,s: str, k: int) -> int:
        ans=0
        dist_count = 0
        for i in range(0, len(s),1):
            dist_count = 0
            val_char = [0] * 26
            for j in range(i,len(s),1):
                if(val_char[ord(s[j]) - 97] == 0):
                    dist_count += 1
                val_char[ord(s[j]) - 97] += 1
                if(dist_count == k):
                    ans += 1
                if(dist_count > k):
                    break
        return ans  
    def longestPalindrome_brute(self, s: str) -> str:
        max_=0
        max_string=""
        new_string=""
        for i in range(0,len(s),1):
            for j in range(i,len(s),1):
                str1=""
                for k in range(i,j+1,1):
                    str1+=s[k]
                new_string=self.checkpalindrome(str1)
                if(new_string==str1):
                    if(len(new_string)>max_):
                        max_string=str1
                        max_=len(str1)

        return max_string
        
    def checkpalindrome(self,str):
        str1="" 
        for i in range(len(str)-1,-1,-1):
            str1+=str[i]
        return str1
    
    def longestPalindrome(self, s: str) -> str:
        result=""
        ans=""
        ans1=""
        for i in range(0,len(s),1):
            ans=self.expand(i,i,s)
            if(len(ans)>len(result)):
                result=ans
            ans1=self.expand(i,i+1,s)
            if(len(ans1)>len(result)):
                result=ans1
        return result
    def expand(self,start,end,str):
        while(start>=0 and end<len(str) and str[start]==str[end]):
            start-=1
            end+=1
        return str[start+1:end]

    def beautySum(self, s: str) -> int:
        ans=0
        for i in range(0,len(s),1):
            val_map={}
            for j in range(i,len(s),1):
                if(s[j] not in val_map):
                  val_map[s[j]]=1
                  ans+=self.findbeauty(val_map)
                else:
                  val_map[s[j]]+=1
                  ans+=self.findbeauty(val_map)
        return ans 

    def findbeauty(self,val_map):
        min_=100000000000
        max_=-999999
        for key in val_map:
            max_=max(max_,val_map[key])
            min_=min(min_,val_map[key])
        return max_ - min_  
#921. Minimum Add to Make Parentheses Valid
    def minAddToMakeValid(self, s):
        if len(s)==1:
            return 1
        stack=[]
        parentheses = {")":"("}
        for i in range(0,len(s),1):
            if stack and stack[-1]==parentheses.get(s[i],None):
                stack.pop()
            else:
                stack.append(s[i])
            i+=1
        return len(stack)
            
#Count and say
    def countAndSay(self, n):
        def dfs(n):
            if n==1:
                return "1"
            prev=dfs(n-1)
            result = ""
            count=1 #intial 1 since a n is give and it has passed it means it has 1
            for i in range(len(prev)):
                #to make sure we are in bounadry
                if i+1<len(prev) and prev[i]==prev[i+1]:
                    #we increment
                    count+=1
                else:
                    # string count that times
                    result += str(count) + prev[i]
                    count=1
            return result
        return dfs(n)
#28. Find the Index of the First Occurrence in a String
    def strStr(self, word, check):
        k=len(check)
        for i in range(0,len(word),1):
            if word[i:i+k]==check:
                return i
        return -1






a=Strings_problems()
s ="babad"
b="nagaram"
ans=a.longestPalindrome(s)
print(ans)