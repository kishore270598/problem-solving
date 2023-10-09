class Solution:
    def lengthOfLastWord(self, s):      
        result=s.split(" ")
        ans=[]
        for element in result:
            if(element.isalpha()):
                ans.append(element)

        return len(ans[-1])
    
    def strStr(self, haystack, needle):
        
        for c in haystack:
            if(c)

        
s=Solution()
k="   fly me   to   the moon  "
ans=s.lengthOfLastWord(k)
print(ans)