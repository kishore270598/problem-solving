class Recursion:
    def fib(self,n):
        firstterm=1
        secondterm=1
        z=[]
        if(n<=0):
            return z
        z.append(firstterm)
        if(n<=1):
            return z
        z.append(secondterm)
        n=n-2
        while(n>0):
            n-=1
            nextterm=firstterm+secondterm
            firstterm=secondterm
            secondterm=nextterm
            z.append(nextterm)
        return z
    def fibrec(self,n):
        if(n<=0):
            return []
        if(n<=1):
            return [1]
        return self.fibrec1(1,1,[1,1],n-2)
    def fibrec1(self,first,second,arr,n):
        if(n==0):
            return arr
        next = first+second
        arr.append(next)
        return self.fibrec1(second,next,arr,n-1)
    def palindrome():
        pass

