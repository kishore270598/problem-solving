class Test:
    def plusOne(self):
        digits=[9]
        val=10
        val=val**(len(digits)-1)
        sums=0
        i=0
        while(val>=1):
            sums+=val*digits[i]
            val=val//10
            i+=1
        if(digits[i-1]==9):
            k=i+1
        else:
            k=i
        sums=sums+1
        z=[]
        val=10
        val=val**(k-1)
        string = str(sums)
        for i in string:
            z.append(int(i))
        print(z)
    
    
    def getRow(self, rowIndex):
        z=[]
        i=0
        while(i<rowIndex):
            value=self.ncr(rowIndex,i)
            z.append(value)
            i+=1
        z.append(1)
        return z

    def ncr(self,k,r):
        return self.fact(k)//(self.fact(r) * self.fact(k-r))
    
    def fact(self,k):
        if k==0:
            return 1
        val=1
        for i in range (2,k+1,1):
            val*=i
        return val
       
a=Test()
result=a.getRow()



