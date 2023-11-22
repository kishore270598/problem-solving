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
                    





            
            
                 
               


          


    
k=Solution()
V = 11
M = 3
coins=[5,5,5,10,20]
ans=k.lemonadeChange(coins)
print(ans)