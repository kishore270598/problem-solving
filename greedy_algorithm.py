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


    
k=greedy()
s=[1,1]
g=[1,2,3]
ans=k.findContentChildren(g,s)
print(ans)