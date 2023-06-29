class Solution:
    def recur(self,i,n):
        if(i>n):
            return
        print('GFG',end=' ')
        self.recur(i+1,n)

    def printGfg(self, n):
        self.recur(1,n)

        # Code here


s=Solution()
n=3
s.printGfg(n)
 



    