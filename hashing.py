class Hashing:
    def findcounts(self, arr, queries):
        z=[]
        for i in range (0,len(queries),1):
            z.append(self.findnum(arr,queries[i]))
        return z
        

    def findnum(self, arr,tofind):
        count=0
        for i in range (0,len(arr),1):
            if(arr[i]==tofind):
                count+=1
        return count

    def findcounthasing(self,arr,queries):
        hash = [0]
        hash = hash * 256
        # pre-processing
        for i in range (0,len(arr),1):
            hash[ord(arr[i])]+=1
        # finding            
        z = []
        for i in range (0,len(queries),1):
           char = queries[i] #a b E
           z.append(hash[ord(char)])            
        return z
    def findcountsdic(self,arr,queries):
        count={}
        # pre-processing
        for key in arr:
            # if value present in dictionary , add 1 to it
            if key in count:
                count[key] = count[key] + 1
            # if value not present, put key,value(key, 1) in dictionary
            else:
                count[key] = 1
        # finding   
        z=[]
        for tofind in queries:
            #quereis value==dic check
            #dic key check (tofind)
            if tofind in count:
                z.append(count[tofind])
            else:
                z.append(0)  
        return z  
    def find_counts_string(self, word):
        z={}
        for key in word:
            if (key==' '):
                continue
            if key in z:
                z[key]=z[key]+1
            else:
                z[key]=1
        print(z)
        for key,value in z.items():
            print('char:',key,' count:',value)
    def findcounttopk(self,nums,k):
        count={}
        z=[]
        for key in nums:
            if key in count:
                count[key] = count[key]  + 1
            else:
                count[key] = 1
        for key,value in count.items():
            z.append((value,key))
        sorted_z = sorted(z, reverse=True)
        res = []
        for i in range (0,k,1):
            sorted_pair = sorted_z[i] #(3, 1)
            res.append(sorted_pair[1])
        return res

