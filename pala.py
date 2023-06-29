class Solution:
    def pal(self,i):
        lens=len(arr)
        if(i>=(lens//2)):
             return 'YES'
        if(arr[i]!=arr[lens-i-1]):
                return 'No'
        return self.pal(i+1)

arr='MADAMzx'
s=Solution()
print(s.pal(0))



