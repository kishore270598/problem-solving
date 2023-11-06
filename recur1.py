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

    def palindrome_itr(self,string,temp,i):
        if string==temp:
            return True
        if(len(string)==len(temp)):
            return False
        return self.palindrome_itr(string,string[i]+temp,i+1)

    def palindrome_rec(self,string): #mam
        # parameter --- >temp, i,str
        temp=""
        #base
        def palindrome_itr(string,temp,i):
            if string == temp:
                print('True')
                return
            if (len(string)==len(temp)):
                print('Flase')
                return
            palindrome_itr(string,string[i]+temp,i+1)

        print(palindrome_itr(string,temp,0))

r=Recursion()
s="mam"
r.palindrome_rec(s)
