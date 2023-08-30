import time
import math
class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class Linked_list:
    def __init__(self):
        self.head=None
        # self.tail=None
    #normal insertion
    def insertion(self,data):
        node=Node(data,None)
        if self.head is None:
            self.head=node
        else:
            pointer=self.head
            while pointer.next is not None: #O(N)
                pointer=pointer.next
            pointer.next=node
    #insert at begin
    def insert_at_begin(self,data):
        node=Node(data,None)
        if self.head is not None:
            node.next =self.head 
        self.head=node
    

    def delete_last(self):
        if self.head is None:
            return 
        if self.head.next is None:
            self.head =None
        pointer=self.head
        while pointer.next.next is not None:
            pointer=pointer.next
        pointer.next=None
    
    def print_all(self):
        current=self.head
        ll=[]
        while current is not None:
            ll.append(current.data)
            current=current.next
        print(ll)

    def findlistlength(self):
        pointer=self.head 
        count=0
        while pointer is not None:
            count+=1
            pointer=pointer.next
        return count 

    def findtheelement(self,k):
        pointer=self.head
        while pointer is not None:
            if(pointer.data==k):
                return 1
            pointer=pointer.next
        return 0
    def delete_k_element(self,k):
        #head element check
        pointer=self.head
        if self.head is None:
            return 
        if(self.head.data==k):
            to_delete = self.head
            self.head = self.head.next
            to_delete.next=None
            return
        previous=None
        while pointer is not None:
            if(pointer.data==k):
                previous.next=pointer.next          
            previous=pointer
            pointer=pointer.next 
    
    def delete_without_head(self, node):
        node.val = node.next.val
        node.next = node.next.next

    def middleNode(self):
        fast=self.head
        slow=self.head
        #Tortoise and Hare method
        while((fast is not None) and (fast.next is not None) ):
            slow=slow.next
            fast=fast.next.next
        return slow 
    def reverseList(self, head: Optional[ListNode]):  
        # we need to create a dummy node which holds null
        temp=None
        cur=head
        while ( head is not None):
            cur=cur.next
            #reversing the arrow
            head.next=temp
            #carrying the head
            temp=head
            head=cur
        return temp
    def hasCycle_brute(self, head) -> bool:
        val1=set()
        pointer=self.head
        while pointer is not None:
            if(pointer.val in val1):
                return True
            else:
                val1.add(pointer.val)
            pointer=pointer.next
        return False
    def hasCycle(self, head) -> bool:
        fast=self.head
        slow=self.head
        while((fast is not None) and (fast.next is not None) ):
            slow=slow.next
            fast=fast.next.next
            if(slow==fast):
                return
        return False
            

ll=Linked_list()
ll.insertion(1)
ll.insertion(2)
ll.insertion(3)
ll.insertion(4)
print(ll.middleNode())
print(ll.delete_k_element(1))
print(ll.reverseList())

# [4] -> next = H
# [1, (none)]              ----------->
# None -> [4,(1)]-->[2,(3)]-->[2,(3)]->[3,(none)]->None
#                      C         
#                             P.next     C.next
# set node.next= head
# head = node
#  N -> H       H
#  H = N     