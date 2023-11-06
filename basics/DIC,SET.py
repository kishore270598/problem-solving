
class test:
    def test_fun(self,arr):
        count=dict()
        #count={}
        for i in range(0,len(arr),1):
            if arr[i] in count:
                count[arr[i]]=i
            else:
                count[arr[i]]=i
        return count

t=test()
a=[1,2,3,4,5,2,4,5]
ans=t.test_fun(a)
print(ans)
