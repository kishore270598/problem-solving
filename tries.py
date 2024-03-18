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
