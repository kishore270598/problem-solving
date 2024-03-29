class Node:
    def __init__(self):
        self.child=[None]*26
        self.endword=False

class Trie(object):
    def __init__(self):
        #root 
        self.root=Node()
    #function to check there exists a char in the trie:
    def return_ord(self,s):
        return ord(s)-ord('a')


    def insert(self, word): #O(n) time O(N*M) SPACE m is char
        #pointer which points to the root
        parent=self.root
        length=len(word)
        #we need to check each char is in the trie or not
        for i in range(0,length,1):
            # it will return the index of ascii
            index=self.return_ord(word[i])
            #if its in my trie
            if not parent.child[index]:
                parent.child[index]=Node()
            #Moving the pointer 
            parent=parent.child[index]
        # at end setting the 
        parent.endword=True

    #O(N) time O(1)space
    def search(self, word):
        parent=self.root
        length=len(word)
        for i in range(length):
            index=self.return_ord(word[i]) 
            if not parent.child[index]:
                return False
            parent=parent.child[index]
        return parent.endword
            
    def startsWith(self, prefix):
        parent=self.root
        length=len(prefix)
        for i in range(length):
            index=self.return_ord(prefix[i]) 
            if not parent.child[index]:
                return False
            parent=parent.child[index]
        return True

class Node1:
    def __init__(self):
        self.child=[None]*26
        self.endcount=0
        self.countprev=0

class Trie:
    def __init__(self):
        self.root=Node1()
         
    def get_ord(self,s):
        return ord(s)-ord('a')

    def insert(self, word):
        length=len(word)
        parent=self.root
        for i in range(length):
            index=self.get_ord(word[i])
            if not parent.child[index]:
                parent.child[index]=Node1()
            parent=parent.child[index]
            parent.countprev+=1
        parent.endcount+=1

    def countWordsEqualTo(self, word):
        parent=self.root
        length=len(word)
        for i in range(length):
            index=self.get_ord(word[i]) 
            if not parent.child[index]:
                return 0
            parent=parent.child[index]
        return parent.endcount

    def countWordsStartingWith(self, word):
        parent=self.root
        length=len(word)
        for i in range(length):
            index=self.get_ord(word[i]) 
            if not parent.child[index]:
                return 0
            parent=parent.child[index]
        return parent.countprev


    def erase(self, word):
        parent=self.root
        length=len(word)
        for i in range(length):
            index=self.get_ord(word[i]) 
            if not parent.child[index]:
                return 0
            parent=parent.child[index]
            parent.countprev-=1
        parent.endcount-=1
#Maximum XOR of Two Numbers in an Array#
class TrieNode:
    def __init__(self):
        self.children = dict()                        
        # children nodes
        self.val = 0                                  
        # end value 

class Trie:
    def __init__(self, n):
        self.root = TrieNode()                        
        # root node
        self.n = n                                    
        # max length of all numbers
        
    def add_num(self, num):
        node=self.root #to point the root
        for shift in range(self.n,-1,-1):
            val = 1 if num & (1 << shift) else 0
            if val not in node.children:
                node.children[val]=TrieNode()
            node = node.children[val]
        node.val=num #to save the value

class Solution:
    def findMaximumXOR(self, nums):
        #to find the maximum n required
        max_len = len(bin(max(nums))) - 2
        trie = Trie(max_len)
        for element in nums:
            trie.add(element)
        for num in nums:
            ans=0
            node = trie.root 
            for shift in range(self.n,-1,-1):
                val = 1 if num & (1 << shift) else 0
                node = node.children[1-val] if 1-val in node.children else node.children[val]
                #take the op
                node = node.children[1-val] if 1-val in node.children else node.children[val] 
            #we need to get the correct last value
            ans=max(ans,nums ^ node.val)
        return ans 
#Maximum XOR With an Element From Array
class Trie:
    def __init__(self):
        self.root={}
        self.m=0
    
    def insert(self,word):
        node=self.root
        for ch in word:
            if ch not in node:
                node[ch]={}
            node=node[ch]

    def compare(self,word,x):
        node=self.root
        t=""
        a,b='0','1'
        for ch in word:
            if ch==a and b in node:
                t+=b
                node=node[b]
            elif ch==b and a in node:
                t+=a
                node=node[a]
            else:
                t+=ch
                node=node[ch]
        ans=int(t,2)^x
        return ans

class Solution:
    def maximizeXor(self, nums, queries):
        trie=Trie()
        n,l=len(queries),len(nums)
        for i in range(n):
            queries[i].append(i)
        queries.sort(key=lambda x:x[1])
        nums.sort()
        res=[0]*n
        j=0
        m=nums[0]
        for i in range(n):
            x,y,z=queries[i][0],queries[i][1],queries[i][2]
            if m>y:
                res[z]=-1
                continue
            while j<l and nums[j]<=y:
                word="{:032b}".format(nums[j])
                trie.insert(word)
                j+=1
            word="{:032b}".format(x)
            ans=trie.compare(word,x)
            res[z]=ans
            t=y
        return res