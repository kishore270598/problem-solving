class Solution:
    def lengthOfLastWord(self, s):      
        result=s.split(" ")
        ans=[]
        for element in result:
            if(element.isalpha()):
                ans.append(element)

        return len(ans[-1])
    
    def strStr(self, string):
        #abddc
        count={}
        c=''
        uniq_char=set()
        arr_char=[0]*26
        for element in range(0,len(string),1):
            k=ord(string[element])
            arr_char[k-97]+=1
        for element in range(0,len(string),1):
            ch=(string[element])
            uniq_char.add(string[element])
        print(uniq_char)
    
    def splitNum(self, num: int) -> int:
        z=[]
        while num!=0:
            z.append(num%10)
            num=num//10
        z=sorted(z)
        a=''
        b=''
        for i in range(len(z)):
            if(i%2==0):
                a+=str(z[i])
            else:
                b+=str(z[i])

        a=int(a)
        b=int(b)
        return a+b

        
s=Solution()
k="abddc"
ans=s.strStr(k)
print(ans)