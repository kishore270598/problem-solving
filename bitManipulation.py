import math
class Bitmanipulation():
    def bitManipulation(self,num,i):
            ans=[]
            mask=1<<(i-1)
            if(mask&num):
                ans.append(1)
            else:
                ans.append(0)
            ans.append(mask | num )
            zeroz=0<<i-1
            ans.append(num&(~mask))
            return ans 
    def oddEven(self,N):
         if(N&1==0):
              return 'even'
         else:
              return 'odd'
    def isPowerOfTwo(self, x: int) -> bool:
        if((n & (n-1))==0):
            return True
        else:
            return False
    def countSetBits(self,N: int) -> int:
        count=0
        K=N
        for i in range(1,K+1,1):
            #010 * 1 -- 0 # right shift001 * 1 -1 count-1
            while(i!=0):
                if((i & 1) ==1):
                    count+=1
                i=i>>1
        return count
    #even (x//2=y)
    # no of set bits of x will be equal to no of set bits of y
    # odd 
    # no of set bits of x will =  1+ no of set bit of y since we divide the 2 (right shift we lose the 1 )  
    def git (self,N: int) -> int:
        count=[0]*(N+1)
        count[0]=0
        for i in range(1,N+1,1):
            count[i]=count[i//2] +i%2
        return sum(count) 
    def countSetBits(self,N: int) -> int:
        ans=0
        d=2
        x=N
        while(x):
            ans+=((N+1)//d)*(d//2) + max((N+1)%d-d//2,0)
            d*=2
            x/=2
        return ans     
    def setBits(self,N):    
        temp=N
        x=1
        flag=1
        while(temp!=0):
            if((N & x)==0):
                flag=0
                break
            x=x<<1
            temp=temp>>1
        if(flag==0):
            return N+x
        else:
            return N
    def swapNumber(self,a,  b):
        a=a^b
        b=a^b
        a=a^b
        return a,b
    
    def divide(self, dividend, divisor):
        if divisor == 0:
            return 2**31 - 1

        # Handle overflow case
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        if((dividend < 0 and divisor >0) or (dividend > 0 and divisor <0)  ):
            negative=-1
        else:
            negative=1

        dividend=abs(dividend)
        divisor=abs(divisor)
        q=0
        for i in range(31,-1,-1):
            if(divisor<<i <=dividend): # add the pow(2,i) 
                dividend -= (divisor << i)
                q+=1<<i # ith value will be the q
        q=q*negative
        if not (-2**31 <= q <= 2**31-1):
            return 2**31 - 1
        else:
            return q
    #to check how many steps needed to change the start to goal
    #checking each last digit and doing right shift
    def minBitFlips(self, start: int, goal: int) -> int:
        count=0
        while (start or goal):
          lastdigits=start & 1
          lastdigitg=goal & 1
          if(lastdigits !=lastdigitg):
              count+=1
          start=start>>1
          goal=goal>>1
        return count
    #find the missing number using bit
    #using xor we can find it
    def singleNumber(self, arr):
        miss=0
        for i in range(0,len(arr),1):
            miss=miss^arr[i]
        return miss

    def subsets(self, nums):
        n=len(nums)
        ans=[]
        for i in range(0,2**n,1):
            ans1=[]
            for j in range(0,n,1):
                if(i&(1<<j)==0):
                    ans1.append(nums[j])
            ans.append(ans1)
        return ans
    def twoOddNum(arr):
        setbit=0
        xor=arr[0]
        first=0
        second=0
        for i in range (1,len(arr),1):
            xor=xor ^ arr[i]
        # we wil get the 2 elements of the odd occurence
        #now we need to split it into
        # Get one set bit in the xor2. We get
        # rightmost set bit in the following
        # line as it is easy to get
        setbit=xor & ~(xor -1)
        for i in range(0,len(arr),1):
            if(arr[i]&setbit==0):
                first=first ^ arr[i]
            else:
                second=second ^ arr[i]
        if(first>second):
            return first,second
        else:
            return second,first

    def countPrimes(self,n):
        a=set()
        for i in range(2,n+1,1):
            while(n%i==0):
                a.add(i)
                n=n//i
        return a



      
    


b=Bitmanipulation()
nums=[1,2,3]
ans=b.countPrimes(17)
print(ans)