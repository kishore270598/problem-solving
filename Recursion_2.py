import time
import math
class Recursion_problems:
    def myPow(self, x: float, n: int) -> float:
        ans=1.0
        k=n
        if(k<0):
            n*=-1
        while(n<0):
            if(n==0):
                return 1
            if(n%2==0):
                ans=x*x
                n=n//2
            else:
                ans=ans*x
                n=n-1
        if(k<0):
            return 1.0/ans
        else:
            return ans
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n == -1:
            return 1/x
        return self.myPow(x, n//2) * self.myPow(x, n//2) * self.myPow(x, n%2)
    #2^10-- > 2^5 * 2^5 
    # 2^5---> 2^(5//2) *2^(5//2) * 2^5%2

    def myAtoi(self, s: str) -> int:
        def rec_atoi(s,i,n,digitsStarted,ans):
            if i>=n:
                return ans
            if digitsStarted:    
                if s[i].isdigit():
                    ans = ans*10 + int(s[i])
                    return rec_atoi(s, i+1,n, True, ans)
                else:
                    return ans
            if s[i] == ' ':
                return rec_atoi(s, i+1,n, False, ans)
                
            if s[i] == '-':
                return -1 * rec_atoi(s, i+1,n, True, ans)

            if s[i] == '+':
                return rec_atoi(s, i+1,n, True, ans)
                        
            if s[i].isdigit():
                return rec_atoi(s, i+1, n, True, int(s[i]))
            return 0
                
        maxInt=2**31 - 1
        minInt=-2**31    
        ans=rec_atoi(s,0,len(s),False,0)
        if ((ans)>maxInt):
            return maxInt
        elif ((ans)<=minInt):
            return minInt
        return ans
        
    def countGoodNumbers_brute(self, n: int) -> int:
        count=1
        for i in range(0,n,1):
            if(i%2==0):
                count=count*5
            else:
                count=count*4

        return count 

    def countGoodNumbers(self, n: int) -> int:
        mod=1000000007
        odd=n//2
        even=n//2+n%2
        return (self.binaryExp(5,even)%mod *self.binaryExp(4,odd)%mod)%mod
    
    def binaryExp(self, x, n):
        mod=1000000007
        if (n==0):
            return 1
        if (n<0):
            return 1/self.binaryExp(x, -n)
        if (n%2==0):
            return self.binaryExp((x*x)%mod, n//2)
        else:
            return x*self.binaryExp((x*x)%mod,(n-1)//2) 


        

