class greedy:
    #Assign Cookies
    def findContentChildren(self, g, s):
        g=sorted(g)
        s=sorted(s)
        left=0
        right=0
        while (left <len(g) and right<len(s)):
            if(g[left]<s[right]):
                left+=1
                right+=1
            else:
                right+=1
        return left
    

class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,arr,n):
        arr.sort(key=lambda x: x.value/x.weight ,reverse=True)
        weight=0
        currentweight=0
        finalvalue=0.0
        remain=0
        
        for i in range(0,len(arr),1):
            if currentweight+arr[i].weight <=W :
                currentweight+=arr[i].weight
                finalvalue+=arr[i].value
            else:
                remain=W-currentweight
                finalvalue+=(arr[i].value /arr[i].weight) *remain
                break
        return finalvalue 
    
    def minCoins(self, coins, M, V):
        right=0
        coins_=sorted(coins,reverse=True)
        res=set()
        current_sum=0
        for i in range(0,len(coins_),1):
            while V>=coins_[i]:
                V-=coins_[i]
                res.add(coins_[i])
        return res
    
    def lemonadeChange(self, bills):
        current_change=0
        if(bills[0]!=5):
            return False
        current_change=5    
        for i in range(1,len(bills),1):
            if(bills[i]==10):
                if(current_change<5):
                    return False
                current_change+=5
            elif(bills[i]==20):
                if(current_change<15):
                    return False
                else:
                    current_change-=10
            else:
                current_change+=5
        return True

    def checkValidString(self, s):
        #we will be holding 2 var 
        # with * possible as left left max and *  as right left min
        left_min=0
        left_max=0
        for c in s:
            if(c=='('):
                left_max+=1
                left_min+=1
            elif(c==')'):
                left_max-=1
                left_min-=1
            else:
                left_max+=1
                left_min-=1
            if(left_max<0):
                return False
            if(left_min<0):
                left_min=0
        return left_min==0
    
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if(numOnes>=k):
            return k
        current_max=0
        while(k>0):
            if(numOnes!=0 and numOnes<k):
                current_max+=numOnes
                k-=1*(numOnes)
                numOnes=0
            elif(numZeros!=0 and k!=0):
                k-=1*(numZeros)
                numZeros=0
            elif(k!=0):
                current_max+=k*(-1)
                k=0
        return current_max


   
k=Solution()
V = 11
M = 3
s='011100'
ans=k.kItemsWithMaximumSum(3,2,0,4)
print(ans)