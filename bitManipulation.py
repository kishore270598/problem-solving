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


b=Bitmanipulation()
ans=b.swapNumber(3,2)
print(ans)