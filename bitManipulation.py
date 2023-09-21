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
         





b=Bitmanipulation()
ans=b.bitManipulation(128,7)
print(ans)